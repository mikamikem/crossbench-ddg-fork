# Copyright 2023 The Chromium Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations

import os

from typing_extensions import override

from crossbench.browsers.attributes import BrowserAttributes
from crossbench.browsers.chromium_based.chromium_based import ChromiumBased
from crossbench.browsers.ddg.base import DDGBaseMixin
from crossbench.browsers.settings import Settings
from crossbench.flags.base import Flags
from crossbench.flags.chrome import ChromeFlags


class DDG(DDGBaseMixin, ChromiumBased):
  DEFAULT_FLAGS = (
      "--no-onboarding", # Currently will only work in DEBUG builds
  )

  @classmethod
  @override
  def attributes(cls) -> BrowserAttributes:
    return BrowserAttributes.DDG | BrowserAttributes.CHROMIUM_BASED

  @override
  def _init_flags(self, settings: Settings) -> ChromeFlags:
    flags: Flags = super()._init_flags(settings)

    if os.path.exists('remoteConfigOverride.json'):
        self._flags.set("--force-remote-config-source",
                        os.path.join(os.getcwd(), 'remoteConfigOverride.json'))
