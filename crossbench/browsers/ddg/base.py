# Copyright 2025 The Chromium Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations

from typing import TYPE_CHECKING, Type

from crossbench.browsers.ddg.version import DDGVersion

if TYPE_CHECKING:
  from crossbench import plt
  from crossbench.browsers.chromium.version import ChromiumVersion
  from crossbench.path import AnyPath


class DDGBaseMixin:

  @classmethod
  def version_cls(cls) -> Type[ChromiumVersion]:
    return DDGVersion

  @classmethod
  def default_path(cls, platform: plt.Platform) -> AnyPath:
    return cls.stable_path(platform)

  @classmethod
  def stable_path(cls, platform: plt.Platform) -> AnyPath:
    return platform.search_app_or_executable(
        "DDG Stable",
        macos=["Microsoft Edge.app"],
        linux=["microsoft-edge"],
        win=["Microsoft/WindowsApps/DuckDuckGo.DesktopBrowser_ya2fgkz3nks94/DuckDuckGo.exe"])

  @classmethod
  def beta_path(cls, platform: plt.Platform) -> AnyPath:
    return platform.search_app_or_executable(
        "DDG Beta",
        macos=["Microsoft Edge Beta.app"],
        linux=["microsoft-edge-beta"],
        win=["Microsoft/WindowsApps/DuckDuckGo.DesktopBrowserBeta_ya2fgkz3nks94/DuckDuckGo.exe"])

  @classmethod
  def dev_path(cls, platform: plt.Platform) -> AnyPath:
    return platform.search_app_or_executable(
        "DDG Preview",
        macos=["Microsoft Edge Dev.app"],
        linux=["microsoft-edge-dev"],
        win=["Microsoft/WindowsApps/DuckDuckGo.DesktopBrowserPreview_ya2fgkz3nks94/DuckDuckGo.exe"])

  @classmethod
  def canary_path(cls, platform: plt.Platform) -> AnyPath:
    return platform.search_app_or_executable(
        "DDG Canary",
        macos=["Microsoft Edge Canary.app"],
        linux=[],
        win=["Microsoft/WindowsApps/DuckDuckGo.DesktopBrowserCanary_ya2fgkz3nks94/DuckDuckGo.exe"])

  @classmethod
  def type_name(cls) -> str:
    return "ddg"
