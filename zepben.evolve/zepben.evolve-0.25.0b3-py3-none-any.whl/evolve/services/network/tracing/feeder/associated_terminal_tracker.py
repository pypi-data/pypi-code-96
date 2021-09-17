#  Copyright 2021 Zeppelin Bend Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Optional

from zepben.evolve.model.cim.iec61970.base.core.terminal import Terminal
from zepben.evolve.services.network.tracing.traversals.tracker import Tracker

__all__ = ["AssociatedTerminalTracker"]


class AssociatedTerminalTracker(Tracker):
    """A tracker that tracks the `ConductingEquipment` that owns the `Terminal` regardless of how it is visited."""

    def has_visited(self, terminal: Optional[Terminal]):
        # Any terminal that does not have a valid conducting equipment reference is considered visited.
        if terminal is not None:
            if terminal.conducting_equipment is not None:
                return terminal.conducting_equipment in self.visited
        return True

    def visit(self, terminal: Optional[Terminal]):
        # We don't visit any terminal that does not have a valid conducting equipment reference.
        if terminal is not None:
            if terminal.conducting_equipment is not None:
                self.visited.add(terminal.conducting_equipment)
                return True
        return False
