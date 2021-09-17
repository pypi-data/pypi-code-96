"""Implements Latent Class Model."""

from .multinomial_logit import MultinomialLogit
import numpy as np
from scipy.optimize import minimize

# define the computation boundary values not to be exceeded
min_exp_val = -700
max_exp_val = 700

max_comp_val = 1e+300
min_comp_val = 1e-300


class LatentClassModel(MultinomialLogit):
    """Class for estimation of Latent Class Models."""
    def __init__(self):
        super(LatentClassModel, self).__init__()

    def fit(self, X, y, varnames=None, alts=None, isvars=None, num_classes=2,
            class_params_spec=None, member_params_spec=None,
            ids=None, weights=None, avail=None, transvars=None,
            transformation=None, base_alt=None, fit_intercept=False,
            init_coeff=None, maxiter=2000, random_state=None, ftol=1e-5,
            gtol=1e-5, grad=True, hess=True, panels=None, verbose=1,
            method="bfgs", scipy_optimisation=False):
        """Fit multinomial and/or conditional logit models.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_variables)
            Input data for explanatory variables in long format

        y : array-like, shape (n_samples,)
            Choices in long format

        varnames : list, shape (n_variables,)
            Names of explanatory variables that must match the number and
            order of columns in ``X``

        alts : array-like, shape (n_samples,)
            Alternative indexes in long format or list of alternative names

        isvars : list
            Names of individual-specific variables in ``varnames``

        num_classes: int
            Number of latent classes

        class_params_spec: array-like, shape (n_samples,)
            Array of lists containing names of variables for latent class

        member_params_spec: array-like, shape (n_samples,)
            Array of lists containing names of variables for class membership

        transvars: list, default=None
            Names of variables to apply transformation on

        ids : array-like, shape (n_samples,)
            Identifiers for choice situations in long format.

        transformation: string, default=None
            Name of transformation to apply on transvars

        weights : array-like, shape (n_variables,), default=None
            Weights for the choice situations in long format.

        avail: array-like, shape (n_samples,)
            Availability of alternatives for the choice situations. One when
            available or zero otherwise.

        base_alt : int, float or str, default=None
            Base alternative

        fit_intercept : bool, default=False
            Whether to include an intercept in the model.

        init_coeff : numpy array, shape (n_variables,), default=None
            Initial coefficients for estimation.

        maxiter : int, default=200
            Maximum number of iterations

        random_state : int, default=None
            Random seed for numpy random generator

        verbose : int, default=1
            Verbosity of messages to show during estimation. 0: No messages,
            1: Some messages, 2: All messages

        method: string, default="bfgs"
            specify optimisation method passed into scipy.optimize.minimize

        ftol : int, float, default=1e-5
            Sets the tol parameter in scipy.optimize.minimize - Tolerance for
            termination.

        gtol: int, float, default=1e-5
            Sets the gtol parameter in scipy.optimize.minimize(method="bfgs) -
            Gradient norm must be less than gtol before successful termination.

        grad : bool, default=True
            Calculate and return the gradient in _loglik_and_gradient

        hess : bool, default=True
            Calculate and return the gradient in _loglik_and_gradient

        scipy_optimisation : bool, default=False
            Use scipy_optimisation for minimisation. When false uses own
            bfgs method.

        Returns
        -------
        None.
        """
        self.ftol = ftol
        self.gtol = gtol
        self.num_classes = num_classes

        # default to using all varnames in each latent class if not specified
        if class_params_spec is None:
            class_params_spec = np.array([])
            class_params_spec = np.vstack([varnames for i in range(num_classes)])
        self.class_params_spec = class_params_spec

        if member_params_spec is None:
            member_params_spec = np.vstack([varnames for i in range(num_classes-1)])
        self.member_params_spec = member_params_spec

        self.panels = panels
        self.init_df = X
        self.init_y = y
        self.ids = ids

        super(LatentClassModel, self).fit(X, y, varnames, alts, isvars,
                                          transvars, transformation, ids,
                                          weights, avail, base_alt,
                                          fit_intercept, init_coeff, maxiter,
                                          random_state, ftol, gtol, grad, hess,
                                          verbose, method, scipy_optimisation)

    def optimal_class_fit(self, X, y, varnames=None, alts=None, isvars=None,
                          num_classes=1, class_params_spec=None,
                          member_params_spec=None, ids=None, weights=None,
                          avail=None, transvars=None, transformation=None,
                          base_alt=None, fit_intercept=False, init_coeff=None,
                          maxiter=2000, random_state=None, ftol=1e-5,
                          gtol=1e-5, grad=True, hess=True, panels=None,
                          verbose=1, method="placeholder",
                          scipy_optimisation=False):
        """Determines optimal number of latent classes based on BIC.
           Note current implementation only considers latent classes with
           the same variables."""
        self.num_classes = num_classes
        self.panels = panels
        self.init_df = X
        self.init_y = y
        self.ids = ids

        curr_bic = -1
        prev_bic = 0

        while curr_bic < prev_bic and self.num_classes > 1:  # lowest BIC
            class_params_spec = np.vstack([varnames for i in range(self.num_classes)])
            self.class_params_spec = class_params_spec

            member_params_spec = np.vstack([varnames for i in range(self.num_classes-1)])
            self.member_params_spec = member_params_spec
        
            super(LatentClassModel, self).fit(X, y, varnames, alts, isvars,
                                              transvars, transformation, ids,
                                              weights, avail, base_alt,
                                              fit_intercept, init_coeff,
                                              maxiter, random_state, ftol,
                                              gtol, grad, hess, verbose,
                                              method, scipy_optimisation)
            prev_bic = curr_bic
            curr_bic = self.bic
            self.num_classes -= 1

        if self.num_classes == 1:
            # TODO: compare against multinomial?
            pass

        # check cause of termination
        optimal_num = -1
        if curr_bic > prev_bic:
            optimal_num = self.num_classes+2
        else:
            optimal_num = self.num_classes+1

        print('Optimal number of classes', optimal_num)

    def _post_fit(self, optimization_res, coeff_names, sample_size,
                  hess_inv=None, verbose=1):
        new_coeff_names = np.array([])
        for i in range(self.num_classes):
            class_coeff_names = coeff_names[self._get_class_X_idx(i)]
            class_coeff_names = np.core.defchararray.add('class-' + str(i+1) +
                                                         ': ', class_coeff_names)
            new_coeff_names = np.concatenate((new_coeff_names, class_coeff_names))

        super(LatentClassModel, self)._post_fit(optimization_res,
                                                new_coeff_names,
                                                sample_size)

    def _compute_probabilities(self, betas, X, y, avail):
        XB = np.einsum('npjk,k -> npj', X, betas)  # TODO? CHECK
        XB = XB.reshape((self.N, self.P, self.J))
        XB[XB > max_exp_val] = max_exp_val  # avoiding infs
        XB[XB < min_exp_val] = min_exp_val  # avoiding infs

        eXB = np.exp(XB)  # (N, P, J)

        if avail is not None:
            eXB = eXB*avail
        p = np.divide(eXB, np.sum(eXB, axis=2, keepdims=True),
                      out=np.zeros_like(eXB))  # (N,J)

        p[np.isposinf(p)] = max_comp_val
        p[np.isneginf(p)] = min_comp_val

        if hasattr(self, 'panel_info'):
            p = p*self.panel_info[:, :, None]  # Zero for unbalanced panels

        p = y*p

        # collapse on alts
        pch = np.sum(p, axis=2)  

        if hasattr(self, 'panel_info'):
            pch2 = self._prob_product_across_panels(pch, self.panel_info)

        return pch2.flatten()

    def _prob_product_across_panels(self, pch, panel_info):
        if not np.all(panel_info):  # If panels unbalanced. Not all ones
            idx = panel_info == .0
            pch[:, :][idx] = 1  # Multiply by one when unbalanced
        pch = pch.prod(axis=1, dtype=np.float64)  # (N,R)
        pch[pch < min_comp_val] = min_comp_val
        return pch  # (N,R)

    def _balance_panels(self, X, y, panels):
        """Balance panels if necessary and produce a new version of X and y.

        If panels are already balanced, the same X and y are returned. This
        also returns panel_info, which keeps track of the panels that needed
        balancing.
        """
        _, J, K = X.shape
        _, p_obs = np.unique(panels, return_counts=True)
        p_obs = (p_obs/J).astype(int)
        N = len(p_obs)  # This is the new N after accounting for panels
        P = np.max(p_obs)  # panels length for all records
        if not np.all(p_obs[0] == p_obs):  # Balancing needed
            y = y.reshape(X.shape[0], J, 1)
            Xbal, ybal = np.zeros((N*P, J, K)), np.zeros((N*P, J, 1))
            panel_info = np.zeros((N, P))
            cum_p = 0  # Cumulative sum of n_obs at every iteration
            for n, p in enumerate(p_obs):
                # Copy data from original to balanced version
                Xbal[n*P:n*P + p, :, :] = X[cum_p:cum_p + p, :, :]
                ybal[n*P:n*P + p, :, :] = y[cum_p:cum_p + p, :, :]
                panel_info[n, :p] = np.ones(p)
                cum_p += p
        else:  # No balancing needed
            Xbal, ybal = X, y
            panel_info = np.ones((N, P))
        self.panel_info = panel_info  # TODO: bad code
        return Xbal, ybal, panel_info

    def _posterior_est_latent_class_probability(self, class_thetas, X, k):
        """ """
        if class_thetas.ndim == 1:
            class_thetas = class_thetas.reshape(self.num_classes - 1, -1)

        class_thetas_base = np.zeros(k)

        eZB = np.zeros((self.num_classes, self.N))
        
        base_X_idx = self._get_member_X_idx(0)
        zB_q = np.dot(class_thetas_base[None, :], np.transpose(self.short_df[:, base_X_idx]))
        
        eZB[0, :] = np.exp(zB_q)
        
        for i in range(1, self.num_classes):
            class_X_idx = self._get_member_X_idx(i)
            zB_q = np.dot(class_thetas[i-1, :], np.transpose(self.short_df[:, class_X_idx]))
            zB_q[np.where(max_exp_val < zB_q)] = max_exp_val
            eZB[i, :] = np.exp(zB_q)

        H = eZB/np.sum(eZB, axis=0, keepdims=True)

        return H

    def _class_member_func(self, class_thetas, weights, X):
        """ TODO """
        k = int(len(class_thetas) / (self.num_classes-1))  # TODO: confirmation
        k = self.member_params_spec[0].size
        H = self._posterior_est_latent_class_probability(class_thetas, X, k)
        # tmp = H - weights
        # grad_df = np.zeros((self.N * self.num_classes, k))
        H[np.where(H < 1e-30)] = 1e-30
        weight_post = np.multiply(np.log(H), weights)
        ll = -np.sum(weight_post)
        return ll

    def _loglik_func(self, betas, X, y, weights, avail):
        """TODO"""
        XB = np.einsum('npjk,k -> npj', X, betas) #TODO? CHECK
        XB = XB.reshape((self.N, self.P, self.J))
        XB[XB > max_exp_val] = max_exp_val  # avoiding infs
        XB[XB < min_exp_val] = min_exp_val  # avoiding infs

        eXB = np.exp(XB)  # (N, P, J)

        if avail is not None:
            eXB = eXB*avail

        p = np.divide(eXB, np.sum(eXB, axis=2, keepdims=True), out=np.zeros_like(eXB))  # (N,J)

        p[np.isposinf(p)] = max_comp_val
        p[np.isneginf(p)] = min_comp_val

        if hasattr(self, 'panel_info'):
            p = p*self.panel_info[:, :, None]

        # TODO: testing ... joint prob. estimation panel data
        if hasattr(self, 'panel_info'):
            pch = np.sum(y*p, axis=2, dtype=np.float64)
            pch = self._prob_product_across_panels(pch, self.panel_info)
            pch[pch < min_comp_val] = min_comp_val

        else:
            pch = np.sum(y*p, axis=2)

        lik = pch

        if lik.ndim > 2:
            lik = np.sum(np.sum(lik, axis=2), axis=1)

        if lik.ndim == 2:
            lik = np.sum(lik, axis=1)

        lik[np.where(lik < min_comp_val)] = min_comp_val
        loglik = np.log(lik)

        if weights is not None:
            loglik = loglik*weights

        loglik = np.sum(loglik)
        ymp = y - p
        grad = np.einsum('npj, npjk -> nk', ymp, X)
        if weights is not None:
            grad = grad*weights[:, None]

        grad = np.sum(grad, axis=0)

        return -loglik  #, grad

    def _get_class_X_idx(self, class_num):
            """[summary]  #TODO

            Args:
                class_num ([type]): [description]

            Returns:
                [type]: [description]
            """
            #  below line: return indices of that class params in Xnames
            #  pattern matching for isvars
            X_class_idx = [np.where(np.char.find(self.Xnames, param) != -1)[0]
                           for param in self.class_params_spec[class_num]]
            X_class_idx = np.concatenate([x for x in X_class_idx])  # 0 - only 1 col isvars
            return np.sort(X_class_idx)

    def _get_member_X_idx(self, class_num):
        class_num = 0  # TODO! ASSUMING ONLY ONE MEMBER MEM SPEC ALLOWED!!
        X_class_idx = [np.where(np.char.find(self.Xnames, param) != -1)[0]
                       for param in self.member_params_spec[class_num]]
        X_class_idx = np.concatenate([x for x in X_class_idx])
        return np.sort(X_class_idx)

    def _get_betas_length(self, class_num):
        class_params_spec = self.class_params_spec[class_num]
        class_isvars = [x for x in class_params_spec if x in self.isvars]
        class_asvars = [x for x in class_params_spec if x in self.asvars]
        has_intercept = True if 'intercept' in class_params_spec else False
        numFixedCoeffs = ((len(self.alternatives)-1)*(len(class_isvars)) + len(class_asvars)
                          if not has_intercept
                          else (len(self.alternatives)-1)*(len(class_isvars)+1) + len(class_asvars))
        return numFixedCoeffs

    def _expectation_maximisation_algorithm(self, betas, X, y, avail):
        """ """
        X = X.reshape(self.N, self.P, self.J, -1)
        y = y.reshape(self.N, self.P, -1)

        converged = False
        class_thetas = np.stack([np.repeat(.0, len(self.member_params_spec[0])) for _ in range(1, self.num_classes)], axis=0)  # class member ship probability
        class_betas = [np.random.normal(0, .1, self._get_betas_length(i)) for i in range(self.num_classes)] # beta vectors for each class
        log_lik_old = 0

        # TODO: extend to panel data?
        k = len(self.varnames)
        short_df = np.zeros((self.N, k))
        original_X = self.initialData
        id_count = 0
        short_ispos = [i for i in range(k) if i not in self.aspos]
        short_df_asvars = np.zeros((len(np.unique(self.ids)), len(self.aspos)))
        short_df_isvars = np.zeros((len(np.unique(self.ids)), len(short_ispos)))
        for id_num in np.unique(self.ids):
            idx = np.where(self.ids == id_num)
            curr_X = np.mean(original_X[idx, :], axis=1)
            if len(self.aspos) > 0:
                short_df_asvars[id_count, :] = curr_X[:, self.aspos]

            if len(short_ispos) > 0:
                short_df_isvars[id_count, :] = curr_X[:, self.ispos]

            id_count += 1

        short_df_isvars = np.tile(short_df_isvars, (1, self.J - 1))

        if len(self.aspos) > 0 and len(short_ispos) > 0:
            short_df = np.hstack((short_df_isvars, short_df_asvars))
        elif len(self.aspos) > 0:
            short_df = short_df_asvars
        elif(short_ispos) > 0:
            short_df = short_df_isvars

        self.short_df = short_df  # store for use..average df over indiv.
        max_iter = 2000
        iter_num = 0
        class_betas_sd = [np.zeros(len(betas))
                          for betas in class_betas]

        while not converged and iter_num < max_iter:
            # Expectation step
            X_class0_idx = self._get_class_X_idx(0)
            p = self._compute_probabilities(class_betas[0],
                                            X[:, :, :,
                                            X_class0_idx],
                                            y,
                                            avail)

            k = len(class_betas[0])

            k = np.atleast_2d(self.member_params_spec)[0].size
            H = self._posterior_est_latent_class_probability(class_thetas,
                                                             X,
                                                             k)
            for class_i in range(1, self.num_classes):
                X_class_idx = self._get_class_X_idx(class_i)
                new_p = self._compute_probabilities(class_betas[class_i],
                                                    X[:, :, :, X_class_idx],
                                                    y,
                                                    avail)
                p = np.vstack((p, new_p))

            weights = np.multiply(p, H)
            weights[weights == 0] = min_comp_val

            lik = np.sum(weights, axis=0)
            lik[np.where(lik < min_comp_val)] = min_comp_val
            log_lik = np.log(np.sum(weights, axis=0))  # sum over classes

            log_lik_new = np.sum(log_lik)

            weights = np.divide(weights, np.tile(np.sum(weights, axis=0), (self.num_classes, 1)))

            # Maximisation step
            opt_res = minimize(self._class_member_func,
                               class_thetas,
                               args=(weights, X),
                               method='BFGS',
                               tol=1e-6,
                               options={'gtol': 1e-6}
                              )
            class_thetas = opt_res['x']
            tmp_thetas_sd = np.sqrt(np.diag(opt_res['hess_inv']))
            for s in range(0, self.num_classes):
                class_X_idx = self._get_class_X_idx(s)
                opt_res = minimize(self._loglik_func,
                                   class_betas[s],
                                   args=(X[:, :, :, class_X_idx],
                                         y,
                                         weights[s, :],
                                         avail),
                                   method="BFGS",
                                   tol=self.ftol,
                                   options={'gtol': self.gtol}
                                   )

                if opt_res['success']:
                    class_betas[s] = opt_res['x']
                    tmp_calc = np.sqrt(np.diag(opt_res['hess_inv']))
                    class_betas_sd[s] = tmp_calc

            converged = np.abs(log_lik_new - log_lik_old) < self.ftol

            log_lik_old = log_lik_new
            iter_num += 1
            class_thetas = class_thetas.reshape((self.num_classes-1, -1))

        x = np.array([])
        for betas in class_betas:
            betas = np.array(betas)
            x = np.concatenate((x, betas))

        stderr = np.concatenate(class_betas_sd)

        optimisation_result = {'x': x, 'success': converged,
                               'fun': log_lik_new, 'nit': iter_num,
                               'stderr': stderr, 'is_latent_class': True,
                               'class_x': class_thetas.flatten(),
                               'class_x_stderr': tmp_thetas_sd}

        return optimisation_result

    def _bfgs_optimization(self, betas, X, y, weights, avail, maxiter):
        """ masking bfgs function in multinomial logit""" 
        opt_res = self._expectation_maximisation_algorithm(betas, X, y, avail)
        return opt_res
