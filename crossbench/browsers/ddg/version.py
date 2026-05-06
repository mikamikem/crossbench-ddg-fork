# Copyright 2025 The Chromium Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations

import re
from typing import Final, Iterable, Optional, Self

from typing_extensions import override

from crossbench.browsers.chromium.version import ChromiumVersion
from crossbench.browsers.version import BrowserVersionChannel


class DDGVersion(ChromiumVersion):

  _PREFIX_RE: Final[re.Pattern] = re.compile(
      rf"duckduckgo(?:{ChromiumVersion.CHANNEL_RE.pattern})? ", re.I)

  _VERSION_MAP: dict[int, tuple[int, int, int, int]] = {
      152: (146, 0, 7680, 165),
      155: (147, 0, 7727, 118),
      156: (147, 0, 7727, 118),
      157: (147, 0, 7727, 118)
  }

  @classmethod
  @override
  def _parse(
      cls,
      full_version: str) -> tuple[tuple[int, ...], BrowserVersionChannel, str]:

      if full_version.startswith("DuckDuckGo 1.0.0+"):
          full_version = "DuckDuckGo 0.155.4.0"

      parsed_ddg_version = super()._parse(full_version)

      return cls._VERSION_MAP[parsed_ddg_version[0][1]], parsed_ddg_version[1], parsed_ddg_version[2]

  @classmethod
  @override
  def _validate_prefix(cls, prefix: Optional[str]) -> bool:
    if not prefix:
      return True
    prefix = prefix.lower()
    if prefix.strip() == "m":
      return True
    return (bool(cls._PREFIX_RE.fullmatch(prefix)) or
            super()._validate_prefix(prefix))

  @classmethod
  @override
  def _validate_suffix(cls, suffix: Optional[str]) -> bool:
    # TODO: Implement me!
    return True

  @classmethod
  def dev(cls, parts: Iterable[int], version_str: str = "") -> Self:
    return cls.alpha(parts, version_str)

  @classmethod
  def canary(cls, parts: Iterable[int], version_str: str = "") -> Self:
    return cls.pre_alpha(parts, version_str)
