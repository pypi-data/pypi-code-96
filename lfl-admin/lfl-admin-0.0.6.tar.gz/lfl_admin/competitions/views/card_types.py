from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from lfl_admin.competitions.models.card_types import Card_types, Card_typesManager


@JsonResponseWithException()
def Card_types_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Card_types.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Card_typesManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Card_types_Add(request):
    return JsonResponse(DSResponseAdd(data=Card_types.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Card_types_Update(request):
    return JsonResponse(DSResponseUpdate(data=Card_types.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Card_types_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Card_types.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Card_types_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Card_types.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Card_types_Info(request):
    return JsonResponse(DSResponse(request=request, data=Card_types.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Card_types_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Card_types.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
