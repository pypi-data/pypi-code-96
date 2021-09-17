# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AVTemplate(AbstractModel):
    """Audio/Video transcoding template

    """

    def __init__(self):
        r"""
        :param Name: Name of an audio/video transcoding template, which can contain 1-20 case-sensitive letters and digits
        :type Name: str
        :param NeedVideo: Whether video is needed. `0`: not needed; `1`: needed
        :type NeedVideo: int
        :param Vcodec: Video codec. Valid values: `H264`, `H265`. If this parameter is left empty, the original video codec will be used.
        :type Vcodec: str
        :param Width: Video width. Value range: (0, 3000]. The value must be an integer multiple of 4. If this parameter is left empty, the original video width will be used.
        :type Width: int
        :param Height: Video height. Value range: (0, 3000]. The value must be an integer multiple of 4. If this parameter is left empty, the original video height will be used.
        :type Height: int
        :param Fps: Video frame rate. Value range: [1, 240]. If this parameter is left empty, the original frame rate will be used.
        :type Fps: int
        :param TopSpeed: Whether to enable top speed codec transcoding. Valid values: `CLOSE` (disable), `OPEN` (enable). Default value: `CLOSE`
        :type TopSpeed: str
        :param BitrateCompressionRatio: Compression ratio for top speed codec transcoding. Value range: [0, 50]. The lower the compression ratio, the higher the image quality.
        :type BitrateCompressionRatio: int
        :param NeedAudio: Whether audio is needed. `0`: not needed; `1`: needed
        :type NeedAudio: int
        :param Acodec: Audio codec. Valid value: `AAC` (default)
        :type Acodec: str
        :param AudioBitrate: Audio bitrate. If this parameter is left empty, the original bitrate will be used.
Valid values: `6000`, `7000`, `8000`, `10000`, `12000`, `14000`, `16000`, `20000`, `24000`, `28000`, `32000`, `40000`, `48000`, `56000`, `64000`, `80000`, `96000`, `112000`, `128000`, `160000`, `192000`, `224000`, `256000`, `288000`, `320000`, `384000`, `448000`, `512000`, `576000`, `640000`, `768000`, `896000`, `1024000`
        :type AudioBitrate: int
        :param VideoBitrate: Video bitrate. Value range: [50000, 40000000]. The value must be an integer multiple of 1000. If this parameter is left empty, the original bitrate will be used.
        :type VideoBitrate: int
        :param RateControlMode: Bitrate control mode. Valid values: `CBR`, `ABR` (default)
        :type RateControlMode: str
        """
        self.Name = None
        self.NeedVideo = None
        self.Vcodec = None
        self.Width = None
        self.Height = None
        self.Fps = None
        self.TopSpeed = None
        self.BitrateCompressionRatio = None
        self.NeedAudio = None
        self.Acodec = None
        self.AudioBitrate = None
        self.VideoBitrate = None
        self.RateControlMode = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.NeedVideo = params.get("NeedVideo")
        self.Vcodec = params.get("Vcodec")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.TopSpeed = params.get("TopSpeed")
        self.BitrateCompressionRatio = params.get("BitrateCompressionRatio")
        self.NeedAudio = params.get("NeedAudio")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.VideoBitrate = params.get("VideoBitrate")
        self.RateControlMode = params.get("RateControlMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedInput(AbstractModel):
    """Channel-associated input

    """

    def __init__(self):
        r"""
        :param Id: Input ID
        :type Id: str
        :param AudioSelectors: Audio selector for the input. There can be 0 to 20 audio selectors.
Note: this field may return `null`, indicating that no valid value was found.
        :type AudioSelectors: list of AudioSelectorInfo
        :param PullBehavior: Pull mode. If the input type is `HLS_PULL` or `MP4_PULL`, you can set this parameter to `LOOP` or `ONCE`. `LOOP` is the default value.
Note: this field may return `null`, indicating that no valid value was found.
        :type PullBehavior: str
        :param FailOverSettings: Input failover configuration
Note: this field may return `null`, indicating that no valid value was found.
        :type FailOverSettings: :class:`tencentcloud.mdl.v20200326.models.FailOverSettings`
        """
        self.Id = None
        self.AudioSelectors = None
        self.PullBehavior = None
        self.FailOverSettings = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        if params.get("AudioSelectors") is not None:
            self.AudioSelectors = []
            for item in params.get("AudioSelectors"):
                obj = AudioSelectorInfo()
                obj._deserialize(item)
                self.AudioSelectors.append(obj)
        self.PullBehavior = params.get("PullBehavior")
        if params.get("FailOverSettings") is not None:
            self.FailOverSettings = FailOverSettings()
            self.FailOverSettings._deserialize(params.get("FailOverSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioPidSelectionInfo(AbstractModel):
    """Audio `Pid` selection.

    """

    def __init__(self):
        r"""
        :param Pid: Audio `Pid`. Default value: 0.
        :type Pid: int
        """
        self.Pid = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioPipelineInputStatistics(AbstractModel):
    """Pipeline input audio statistics.

    """

    def __init__(self):
        r"""
        :param Fps: Audio FPS.
        :type Fps: int
        :param Rate: Audio bitrate in bps.
        :type Rate: int
        :param Pid: Audio `Pid`, which is available only if the input is `rtp/udp`.
        :type Pid: int
        """
        self.Fps = None
        self.Rate = None
        self.Pid = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioSelectorInfo(AbstractModel):
    """Audio selector.

    """

    def __init__(self):
        r"""
        :param Name: Audio name, which can contain 1-32 letters, digits, and underscores.
        :type Name: str
        :param AudioPidSelection: Audio `Pid` selection.
        :type AudioPidSelection: :class:`tencentcloud.mdl.v20200326.models.AudioPidSelectionInfo`
        """
        self.Name = None
        self.AudioPidSelection = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("AudioPidSelection") is not None:
            self.AudioPidSelection = AudioPidSelectionInfo()
            self.AudioPidSelection._deserialize(params.get("AudioPidSelection"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTemplateInfo(AbstractModel):
    """Audio transcoding template.

    """

    def __init__(self):
        r"""
        :param AudioSelectorName: Only `AttachedInputs.AudioSelectors.Name` can be selected. This parameter is required for RTP_PUSH and UDP_PUSH.
        :type AudioSelectorName: str
        :param Name: Audio transcoding template name, which can contain 1-20 letters and digits.
        :type Name: str
        :param Acodec: Audio codec. Valid value: AAC. Default value: AAC.
        :type Acodec: str
        :param AudioBitrate: Audio bitrate. If this parameter is left empty, the original value will be used.
Valid values: 6000, 7000, 8000, 10000, 12000, 14000, 16000, 20000, 24000, 28000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 288000, 320000, 384000, 448000, 512000, 576000, 640000, 768000, 896000, 1024000
        :type AudioBitrate: int
        :param LanguageCode: Audio language code, whose length is always 3 characters.
        :type LanguageCode: str
        """
        self.AudioSelectorName = None
        self.Name = None
        self.Acodec = None
        self.AudioBitrate = None
        self.LanguageCode = None


    def _deserialize(self, params):
        self.AudioSelectorName = params.get("AudioSelectorName")
        self.Name = params.get("Name")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.LanguageCode = params.get("LanguageCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelAlertInfos(AbstractModel):
    """Channel alarm information.

    """

    def __init__(self):
        r"""
        :param Pipeline0: Alarm details of pipeline 0 under this channel.
        :type Pipeline0: list of ChannelPipelineAlerts
        :param Pipeline1: Alarm details of pipeline 1 under this channel.
        :type Pipeline1: list of ChannelPipelineAlerts
        """
        self.Pipeline0 = None
        self.Pipeline1 = None


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self.Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = ChannelPipelineAlerts()
                obj._deserialize(item)
                self.Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self.Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = ChannelPipelineAlerts()
                obj._deserialize(item)
                self.Pipeline1.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelInputStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        r"""
        :param InputId: Input ID.
        :type InputId: str
        :param Statistics: Input statistics.
        :type Statistics: :class:`tencentcloud.mdl.v20200326.models.InputStatistics`
        """
        self.InputId = None
        self.Statistics = None


    def _deserialize(self, params):
        self.InputId = params.get("InputId")
        if params.get("Statistics") is not None:
            self.Statistics = InputStatistics()
            self.Statistics._deserialize(params.get("Statistics"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelOutputsStatistics(AbstractModel):
    """Channel output information.

    """

    def __init__(self):
        r"""
        :param OutputGroupName: Output group name.
        :type OutputGroupName: str
        :param Statistics: Output group statistics.
        :type Statistics: :class:`tencentcloud.mdl.v20200326.models.OutputsStatistics`
        """
        self.OutputGroupName = None
        self.Statistics = None


    def _deserialize(self, params):
        self.OutputGroupName = params.get("OutputGroupName")
        if params.get("Statistics") is not None:
            self.Statistics = OutputsStatistics()
            self.Statistics._deserialize(params.get("Statistics"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelPipelineAlerts(AbstractModel):
    """Channel alarm details.

    """

    def __init__(self):
        r"""
        :param SetTime: Alarm start time in UTC time.
        :type SetTime: str
        :param ClearTime: Alarm end time in UTC time.
This time is available only after the alarm ends.
        :type ClearTime: str
        :param Type: Alarm type.
        :type Type: str
        :param Message: Alarm details.
        :type Message: str
        """
        self.SetTime = None
        self.ClearTime = None
        self.Type = None
        self.Message = None


    def _deserialize(self, params):
        self.SetTime = params.get("SetTime")
        self.ClearTime = params.get("ClearTime")
        self.Type = params.get("Type")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLiveChannelRequest(AbstractModel):
    """CreateStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param Name: Channel name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param AttachedInputs: Inputs to attach. You can attach 1-5 inputs.
        :type AttachedInputs: list of AttachedInput
        :param OutputGroups: Configuration information of the channel’s output groups. Quantity: [1, 10]
        :type OutputGroups: list of StreamLiveOutputGroupsInfo
        :param AudioTemplates: Audio transcoding templates. Quantity: [1, 20]
        :type AudioTemplates: list of AudioTemplateInfo
        :param VideoTemplates: Video transcoding templates. Quantity: [1, 10]
        :type VideoTemplates: list of VideoTemplateInfo
        :param AVTemplates: Audio/Video transcoding templates. Quantity: [1, 10]
        :type AVTemplates: list of AVTemplate
        """
        self.Name = None
        self.AttachedInputs = None
        self.OutputGroups = None
        self.AudioTemplates = None
        self.VideoTemplates = None
        self.AVTemplates = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("AttachedInputs") is not None:
            self.AttachedInputs = []
            for item in params.get("AttachedInputs"):
                obj = AttachedInput()
                obj._deserialize(item)
                self.AttachedInputs.append(obj)
        if params.get("OutputGroups") is not None:
            self.OutputGroups = []
            for item in params.get("OutputGroups"):
                obj = StreamLiveOutputGroupsInfo()
                obj._deserialize(item)
                self.OutputGroups.append(obj)
        if params.get("AudioTemplates") is not None:
            self.AudioTemplates = []
            for item in params.get("AudioTemplates"):
                obj = AudioTemplateInfo()
                obj._deserialize(item)
                self.AudioTemplates.append(obj)
        if params.get("VideoTemplates") is not None:
            self.VideoTemplates = []
            for item in params.get("VideoTemplates"):
                obj = VideoTemplateInfo()
                obj._deserialize(item)
                self.VideoTemplates.append(obj)
        if params.get("AVTemplates") is not None:
            self.AVTemplates = []
            for item in params.get("AVTemplates"):
                obj = AVTemplate()
                obj._deserialize(item)
                self.AVTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLiveChannelResponse(AbstractModel):
    """CreateStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreateStreamLiveInputRequest(AbstractModel):
    """CreateStreamLiveInput request structure.

    """

    def __init__(self):
        r"""
        :param Name: Input name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param Type: Input type
Valid values: `RTMP_PUSH`, `RTP_PUSH`, `UDP_PUSH`, `RTMP_PULL`, `HLS_PULL`, `MP4_PULL`
        :type Type: str
        :param SecurityGroupIds: ID of the input security group to attach
You can attach only one security group to an input.
        :type SecurityGroupIds: list of str
        :param InputSettings: Input settings. For the type `RTMP_PUSH`, `RTMP_PULL`, `HLS_PULL`, or `MP4_PULL`, 1 or 2 inputs of the corresponding type can be configured.
        :type InputSettings: list of InputSettingInfo
        """
        self.Name = None
        self.Type = None
        self.SecurityGroupIds = None
        self.InputSettings = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("InputSettings") is not None:
            self.InputSettings = []
            for item in params.get("InputSettings"):
                obj = InputSettingInfo()
                obj._deserialize(item)
                self.InputSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLiveInputResponse(AbstractModel):
    """CreateStreamLiveInput response structure.

    """

    def __init__(self):
        r"""
        :param Id: Input ID
        :type Id: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreateStreamLiveInputSecurityGroupRequest(AbstractModel):
    """CreateStreamLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param Name: Input security group name, which can contain case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param Whitelist: Allowlist entries. Quantity: [1, 10]
        :type Whitelist: list of str
        """
        self.Name = None
        self.Whitelist = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Whitelist = params.get("Whitelist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLiveInputSecurityGroupResponse(AbstractModel):
    """CreateStreamLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param Id: Security group ID
        :type Id: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreateStreamLivePlanRequest(AbstractModel):
    """CreateStreamLivePlan request structure.

    """

    def __init__(self):
        r"""
        :param ChannelId: ID of the channel for which you want to configure an event
        :type ChannelId: str
        :param Plan: Event configuration
        :type Plan: :class:`tencentcloud.mdl.v20200326.models.PlanReq`
        """
        self.ChannelId = None
        self.Plan = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        if params.get("Plan") is not None:
            self.Plan = PlanReq()
            self.Plan._deserialize(params.get("Plan"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLivePlanResponse(AbstractModel):
    """CreateStreamLivePlan response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DashRemuxSettingsInfo(AbstractModel):
    """DASH configuration information.

    """

    def __init__(self):
        r"""
        :param SegmentDuration: Segment duration in ms. Value range: [1000,30000]. Default value: 4000. The value can only be a multiple of 1,000.
        :type SegmentDuration: int
        :param SegmentNumber: Number of segments. Value range: [1,30]. Default value: 5.
        :type SegmentNumber: int
        :param PeriodTriggers: Whether to enable multi-period. Valid values: CLOSE/OPEN. Default value: CLOSE.
        :type PeriodTriggers: str
        """
        self.SegmentDuration = None
        self.SegmentNumber = None
        self.PeriodTriggers = None


    def _deserialize(self, params):
        self.SegmentDuration = params.get("SegmentDuration")
        self.SegmentNumber = params.get("SegmentNumber")
        self.PeriodTriggers = params.get("PeriodTriggers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLiveChannelRequest(AbstractModel):
    """DeleteStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLiveChannelResponse(AbstractModel):
    """DeleteStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStreamLiveInputRequest(AbstractModel):
    """DeleteStreamLiveInput request structure.

    """

    def __init__(self):
        r"""
        :param Id: Input ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLiveInputResponse(AbstractModel):
    """DeleteStreamLiveInput response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStreamLiveInputSecurityGroupRequest(AbstractModel):
    """DeleteStreamLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param Id: Input security group ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLiveInputSecurityGroupResponse(AbstractModel):
    """DeleteStreamLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeStreamLiveChannelAlertsRequest(AbstractModel):
    """DescribeStreamLiveChannelAlerts request structure.

    """

    def __init__(self):
        r"""
        :param ChannelId: Channel ID
        :type ChannelId: str
        """
        self.ChannelId = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveChannelAlertsResponse(AbstractModel):
    """DescribeStreamLiveChannelAlerts response structure.

    """

    def __init__(self):
        r"""
        :param Infos: Alarm information of the channel’s two pipelines
        :type Infos: :class:`tencentcloud.mdl.v20200326.models.ChannelAlertInfos`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = ChannelAlertInfos()
            self.Infos._deserialize(params.get("Infos"))
        self.RequestId = params.get("RequestId")


class DescribeStreamLiveChannelInputStatisticsRequest(AbstractModel):
    """DescribeStreamLiveChannelInputStatistics request structure.

    """

    def __init__(self):
        r"""
        :param ChannelId: Channel ID
        :type ChannelId: str
        :param StartTime: Start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`
        :type StartTime: str
        :param EndTime: End time for query, which is 1 hour after `StartTime` by default
UTC time, such as `2020-01-01T12:00:00Z`
        :type EndTime: str
        :param Period: Data collection interval. Valid values: `5s`, `1min` (default), `5min`, `15min`
        :type Period: str
        """
        self.ChannelId = None
        self.StartTime = None
        self.EndTime = None
        self.Period = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveChannelInputStatisticsResponse(AbstractModel):
    """DescribeStreamLiveChannelInputStatistics response structure.

    """

    def __init__(self):
        r"""
        :param Infos: Channel input statistics
        :type Infos: list of ChannelInputStatistics
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = ChannelInputStatistics()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLiveChannelLogsRequest(AbstractModel):
    """DescribeStreamLiveChannelLogs request structure.

    """

    def __init__(self):
        r"""
        :param ChannelId: Channel ID
        :type ChannelId: str
        :param StartTime: Start time for query, which is 1 hour ago by default. You can query logs in the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`
        :type StartTime: str
        :param EndTime: End time for query, which is 1 hour after `StartTime` by default
UTC time, such as `2020-01-01T12:00:00Z`
        :type EndTime: str
        """
        self.ChannelId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveChannelLogsResponse(AbstractModel):
    """DescribeStreamLiveChannelLogs response structure.

    """

    def __init__(self):
        r"""
        :param Infos: Pipeline push information
        :type Infos: :class:`tencentcloud.mdl.v20200326.models.PipelineLogInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = PipelineLogInfo()
            self.Infos._deserialize(params.get("Infos"))
        self.RequestId = params.get("RequestId")


class DescribeStreamLiveChannelOutputStatisticsRequest(AbstractModel):
    """DescribeStreamLiveChannelOutputStatistics request structure.

    """

    def __init__(self):
        r"""
        :param ChannelId: Channel ID
        :type ChannelId: str
        :param StartTime: Start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`
        :type StartTime: str
        :param EndTime: End time for query, which is 1 hour after `StartTime` by default
UTC time, such as `2020-01-01T12:00:00Z`
        :type EndTime: str
        :param Period: Data collection interval. Valid values: `5s`, `1min` (default), `5min`, `15min`
        :type Period: str
        """
        self.ChannelId = None
        self.StartTime = None
        self.EndTime = None
        self.Period = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveChannelOutputStatisticsResponse(AbstractModel):
    """DescribeStreamLiveChannelOutputStatistics response structure.

    """

    def __init__(self):
        r"""
        :param Infos: Channel output information
        :type Infos: list of ChannelOutputsStatistics
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = ChannelOutputsStatistics()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLiveChannelRequest(AbstractModel):
    """DescribeStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveChannelResponse(AbstractModel):
    """DescribeStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param Info: Channel information
        :type Info: :class:`tencentcloud.mdl.v20200326.models.StreamLiveChannelInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = StreamLiveChannelInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeStreamLiveChannelsRequest(AbstractModel):
    """DescribeStreamLiveChannels request structure.

    """


class DescribeStreamLiveChannelsResponse(AbstractModel):
    """DescribeStreamLiveChannels response structure.

    """

    def __init__(self):
        r"""
        :param Infos: List of channel information
Note: this field may return `null`, indicating that no valid value was found.
        :type Infos: list of StreamLiveChannelInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = StreamLiveChannelInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLiveInputRequest(AbstractModel):
    """DescribeStreamLiveInput request structure.

    """

    def __init__(self):
        r"""
        :param Id: Input ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveInputResponse(AbstractModel):
    """DescribeStreamLiveInput response structure.

    """

    def __init__(self):
        r"""
        :param Info: Input information
        :type Info: :class:`tencentcloud.mdl.v20200326.models.InputInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = InputInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeStreamLiveInputSecurityGroupRequest(AbstractModel):
    """DescribeStreamLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param Id: Input security group ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveInputSecurityGroupResponse(AbstractModel):
    """DescribeStreamLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param Info: Input security group information
        :type Info: :class:`tencentcloud.mdl.v20200326.models.InputSecurityGroupInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = InputSecurityGroupInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeStreamLiveInputSecurityGroupsRequest(AbstractModel):
    """DescribeStreamLiveInputSecurityGroups request structure.

    """


class DescribeStreamLiveInputSecurityGroupsResponse(AbstractModel):
    """DescribeStreamLiveInputSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param Infos: List of input security group information
        :type Infos: list of InputSecurityGroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = InputSecurityGroupInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLiveInputsRequest(AbstractModel):
    """DescribeStreamLiveInputs request structure.

    """


class DescribeStreamLiveInputsResponse(AbstractModel):
    """DescribeStreamLiveInputs response structure.

    """

    def __init__(self):
        r"""
        :param Infos: List of input information
Note: this field may return `null`, indicating that no valid value was found.
        :type Infos: list of InputInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = InputInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLivePlansRequest(AbstractModel):
    """DescribeStreamLivePlans request structure.

    """

    def __init__(self):
        r"""
        :param ChannelId: ID of the channel whose events you want to query
        :type ChannelId: str
        """
        self.ChannelId = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLivePlansResponse(AbstractModel):
    """DescribeStreamLivePlans response structure.

    """

    def __init__(self):
        r"""
        :param Infos: List of event information
Note: this field may return `null`, indicating that no valid value was found.
        :type Infos: list of PlanResp
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = PlanResp()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DestinationInfo(AbstractModel):
    """Relay destination address.

    """

    def __init__(self):
        r"""
        :param OutputUrl: Relay destination address. Length limit: [1,512].
        :type OutputUrl: str
        :param AuthKey: Authentication key. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthKey: str
        :param Username: Authentication username. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.
        :type Username: str
        :param Password: Authentication password. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.
        :type Password: str
        """
        self.OutputUrl = None
        self.AuthKey = None
        self.Username = None
        self.Password = None


    def _deserialize(self, params):
        self.OutputUrl = params.get("OutputUrl")
        self.AuthKey = params.get("AuthKey")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmKey(AbstractModel):
    """Custom DRM key.

    """

    def __init__(self):
        r"""
        :param Key: DRM key, which is a 32-bit hexadecimal string.
Note: uppercase letters in the string will be automatically converted to lowercase ones.
        :type Key: str
        :param Track: Required for Widevine encryption. Valid values: SD, HD, UHD1, UHD2, AUDIO, ALL.
ALL refers to all tracks. If this parameter is set to ALL, no other tracks can be added.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Track: str
        :param KeyId: Required for Widevine encryption. It is a 32-bit hexadecimal string.
Note: uppercase letters in the string will be automatically converted to lowercase ones.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyId: str
        :param Iv: Required when FairPlay uses the AES encryption method. It is a 32-bit hexadecimal string.
For more information about this parameter, please see: 
https://tools.ietf.org/html/rfc3826
Note: uppercase letters in the string will be automatically converted to lowercase ones.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Iv: str
        """
        self.Key = None
        self.Track = None
        self.KeyId = None
        self.Iv = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Track = params.get("Track")
        self.KeyId = params.get("KeyId")
        self.Iv = params.get("Iv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmSettingsInfo(AbstractModel):
    """DRM configuration information, which takes effect only for HLS and DASH.

    """

    def __init__(self):
        r"""
        :param State: Whether to enable DRM encryption. Valid values: `CLOSE` (disable), `OPEN` (enable). Default value: `CLOSE`
DRM encryption is supported only for HLS, DASH, HLS_ARCHIVE, DASH_ARCHIVE, HLS_MEDIAPACKAGE, and DASH_MEDIAPACKAGE outputs.
        :type State: str
        :param Scheme: This parameter can be set to `CustomDRMKeys` or left empty.
CustomDRMKeys means encryption keys customized by users.
        :type Scheme: str
        :param ContentId: If `Scheme` is set to `CustomDRMKeys`, this parameter is required and should be specified by the user.
        :type ContentId: str
        :param Keys: The key customized by the content user, which is required when `Scheme` is set to CustomDRMKeys.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Keys: list of DrmKey
        """
        self.State = None
        self.Scheme = None
        self.ContentId = None
        self.Keys = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.Scheme = params.get("Scheme")
        self.ContentId = params.get("ContentId")
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = DrmKey()
                obj._deserialize(item)
                self.Keys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventSettingsReq(AbstractModel):
    """Configuration information of an event in the plan

    """

    def __init__(self):
        r"""
        :param EventType: Only `INPUT_SWITCH` is supported currently. If you do not specify this parameter, `INPUT_SWITCH` will be used.
        :type EventType: str
        :param InputAttachment: ID of the input to attach, which is required if `EventType` is `INPUT_SWITCH`
        :type InputAttachment: str
        """
        self.EventType = None
        self.InputAttachment = None


    def _deserialize(self, params):
        self.EventType = params.get("EventType")
        self.InputAttachment = params.get("InputAttachment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventSettingsResp(AbstractModel):
    """Configuration information of an event in the plan

    """

    def __init__(self):
        r"""
        :param EventType: Only `INPUT_SWITCH` is supported currently.
        :type EventType: str
        :param InputAttachment: ID of the input attached, which is not empty if `EventType` is `INPUT_SWITCH`
        :type InputAttachment: str
        """
        self.EventType = None
        self.InputAttachment = None


    def _deserialize(self, params):
        self.EventType = params.get("EventType")
        self.InputAttachment = params.get("InputAttachment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailOverSettings(AbstractModel):
    """Input failover settings

    """

    def __init__(self):
        r"""
        :param SecondaryInputId: ID of the backup input
Note: this field may return `null`, indicating that no valid value was found.
        :type SecondaryInputId: str
        :param LossThreshold: The wait time (ms) for triggering failover after the primary input becomes unavailable. Value range: [1000, 86400000]. Default value: `3000`
        :type LossThreshold: int
        :param RecoverBehavior: Failover policy. Valid values: `CURRENT_PREFERRED` (default), `PRIMARY_PREFERRED`
        :type RecoverBehavior: str
        """
        self.SecondaryInputId = None
        self.LossThreshold = None
        self.RecoverBehavior = None


    def _deserialize(self, params):
        self.SecondaryInputId = params.get("SecondaryInputId")
        self.LossThreshold = params.get("LossThreshold")
        self.RecoverBehavior = params.get("RecoverBehavior")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HlsRemuxSettingsInfo(AbstractModel):
    """HLS protocol configuration.

    """

    def __init__(self):
        r"""
        :param SegmentDuration: Segment duration in ms. Value range: [1000,30000]. Default value: 4000. The value can only be a multiple of 1,000.
        :type SegmentDuration: int
        :param SegmentNumber: Number of segments. Value range: [1,30]. Default value: 5.
        :type SegmentNumber: int
        :param PdtInsertion: Whether to enable PDT insertion. Valid values: CLOSE/OPEN. Default value: CLOSE.
        :type PdtInsertion: str
        :param PdtDuration: PDT duration in seconds. Value range: (0,3000]. Default value: 600.
        :type PdtDuration: int
        :param Scheme: Audio/Video packaging scheme. Valid values: `SEPARATE`, `MERGE`
        :type Scheme: str
        """
        self.SegmentDuration = None
        self.SegmentNumber = None
        self.PdtInsertion = None
        self.PdtDuration = None
        self.Scheme = None


    def _deserialize(self, params):
        self.SegmentDuration = params.get("SegmentDuration")
        self.SegmentNumber = params.get("SegmentNumber")
        self.PdtInsertion = params.get("PdtInsertion")
        self.PdtDuration = params.get("PdtDuration")
        self.Scheme = params.get("Scheme")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputInfo(AbstractModel):
    """Input information.

    """

    def __init__(self):
        r"""
        :param Region: Input region.
        :type Region: str
        :param Id: Input ID.
        :type Id: str
        :param Name: Input name.
        :type Name: str
        :param Type: Input type.
        :type Type: str
        :param SecurityGroupIds: Array of security groups associated with input.
        :type SecurityGroupIds: list of str
        :param AttachedChannels: Array of channels associated with input.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttachedChannels: list of str
        :param InputSettings: Input configuration array.
        :type InputSettings: list of InputSettingInfo
        """
        self.Region = None
        self.Id = None
        self.Name = None
        self.Type = None
        self.SecurityGroupIds = None
        self.AttachedChannels = None
        self.InputSettings = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.AttachedChannels = params.get("AttachedChannels")
        if params.get("InputSettings") is not None:
            self.InputSettings = []
            for item in params.get("InputSettings"):
                obj = InputSettingInfo()
                obj._deserialize(item)
                self.InputSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputSecurityGroupInfo(AbstractModel):
    """Input security group information.

    """

    def __init__(self):
        r"""
        :param Id: Input security group ID.
        :type Id: str
        :param Name: Input security group name.
        :type Name: str
        :param Whitelist: List of allowlist entries.
        :type Whitelist: list of str
        :param OccupiedInputs: List of bound input streams.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OccupiedInputs: list of str
        :param Region: Input security group address.
        :type Region: str
        """
        self.Id = None
        self.Name = None
        self.Whitelist = None
        self.OccupiedInputs = None
        self.Region = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Whitelist = params.get("Whitelist")
        self.OccupiedInputs = params.get("OccupiedInputs")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputSettingInfo(AbstractModel):
    """Input settings information.

    """

    def __init__(self):
        r"""
        :param AppName: Application name, which is used for RTMP_PUSH and can contain 1-32 letters and digits.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppName: str
        :param StreamName: Stream name, which is used for RTMP_PUSH and can contain 1-32 letters and digits.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StreamName: str
        :param SourceUrl: Origin-pull URL, which is used for RTMP_PULL/HLS_PULL/MP4_PULL. Length limit: [1,512].
Note: this field may return null, indicating that no valid values can be obtained.
        :type SourceUrl: str
        :param InputAddress: RTP/UDP input address, which does not need to be entered for the input parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InputAddress: str
        :param SourceType: Source type for stream pulling and relaying. To pull content from private-read COS buckets under the current account, set this parameter to `TencentCOS`; otherwise, leave it empty.
Note: this field may return `null`, indicating that no valid value was found.
        :type SourceType: str
        """
        self.AppName = None
        self.StreamName = None
        self.SourceUrl = None
        self.InputAddress = None
        self.SourceType = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.SourceUrl = params.get("SourceUrl")
        self.InputAddress = params.get("InputAddress")
        self.SourceType = params.get("SourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputStatistics(AbstractModel):
    """Input statistics.

    """

    def __init__(self):
        r"""
        :param Pipeline0: Input statistics of pipeline 0.
        :type Pipeline0: list of PipelineInputStatistics
        :param Pipeline1: Input statistics of pipeline 1.
        :type Pipeline1: list of PipelineInputStatistics
        """
        self.Pipeline0 = None
        self.Pipeline1 = None


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self.Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = PipelineInputStatistics()
                obj._deserialize(item)
                self.Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self.Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = PipelineInputStatistics()
                obj._deserialize(item)
                self.Pipeline1.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogInfo(AbstractModel):
    """Log information.

    """

    def __init__(self):
        r"""
        :param Type: Log type.
It contains the value of `StreamStart` which refers to the push information.
        :type Type: str
        :param Time: Time when the log is printed.
        :type Time: str
        :param Message: Log details.
        :type Message: :class:`tencentcloud.mdl.v20200326.models.LogMessageInfo`
        """
        self.Type = None
        self.Time = None
        self.Message = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Time = params.get("Time")
        if params.get("Message") is not None:
            self.Message = LogMessageInfo()
            self.Message._deserialize(params.get("Message"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogMessageInfo(AbstractModel):
    """Log details.

    """

    def __init__(self):
        r"""
        :param StreamInfo: Push information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StreamInfo: :class:`tencentcloud.mdl.v20200326.models.StreamInfo`
        """
        self.StreamInfo = None


    def _deserialize(self, params):
        if params.get("StreamInfo") is not None:
            self.StreamInfo = StreamInfo()
            self.StreamInfo._deserialize(params.get("StreamInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLiveChannelRequest(AbstractModel):
    """ModifyStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        :param Name: Channel name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param AttachedInputs: Inputs to attach. You can attach 1-5 inputs.
        :type AttachedInputs: list of AttachedInput
        :param OutputGroups: Configuration information of the channel’s output groups. Quantity: [1, 10]
        :type OutputGroups: list of StreamLiveOutputGroupsInfo
        :param AudioTemplates: Audio transcoding templates. Quantity: [1, 20]
        :type AudioTemplates: list of AudioTemplateInfo
        :param VideoTemplates: Video transcoding templates. Quantity: [1, 10]
        :type VideoTemplates: list of VideoTemplateInfo
        :param AVTemplates: Audio/Video transcoding templates. Quantity: [1, 10]
        :type AVTemplates: list of AVTemplate
        """
        self.Id = None
        self.Name = None
        self.AttachedInputs = None
        self.OutputGroups = None
        self.AudioTemplates = None
        self.VideoTemplates = None
        self.AVTemplates = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        if params.get("AttachedInputs") is not None:
            self.AttachedInputs = []
            for item in params.get("AttachedInputs"):
                obj = AttachedInput()
                obj._deserialize(item)
                self.AttachedInputs.append(obj)
        if params.get("OutputGroups") is not None:
            self.OutputGroups = []
            for item in params.get("OutputGroups"):
                obj = StreamLiveOutputGroupsInfo()
                obj._deserialize(item)
                self.OutputGroups.append(obj)
        if params.get("AudioTemplates") is not None:
            self.AudioTemplates = []
            for item in params.get("AudioTemplates"):
                obj = AudioTemplateInfo()
                obj._deserialize(item)
                self.AudioTemplates.append(obj)
        if params.get("VideoTemplates") is not None:
            self.VideoTemplates = []
            for item in params.get("VideoTemplates"):
                obj = VideoTemplateInfo()
                obj._deserialize(item)
                self.VideoTemplates.append(obj)
        if params.get("AVTemplates") is not None:
            self.AVTemplates = []
            for item in params.get("AVTemplates"):
                obj = AVTemplate()
                obj._deserialize(item)
                self.AVTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLiveChannelResponse(AbstractModel):
    """ModifyStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyStreamLiveInputRequest(AbstractModel):
    """ModifyStreamLiveInput request structure.

    """

    def __init__(self):
        r"""
        :param Id: Input ID
        :type Id: str
        :param Name: Input name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param SecurityGroupIds: List of the IDs of the security groups to attach
        :type SecurityGroupIds: list of str
        :param InputSettings: Input settings
For the type `RTMP_PUSH`, `RTMP_PULL`, `HLS_PULL`, or `MP4_PULL`, 1 or 2 inputs of the corresponding type can be configured.
This parameter can be left empty for RTP_PUSH and UDP_PUSH inputs.
Note: If this parameter is not specified or empty, the original input settings will be used.
        :type InputSettings: list of InputSettingInfo
        """
        self.Id = None
        self.Name = None
        self.SecurityGroupIds = None
        self.InputSettings = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("InputSettings") is not None:
            self.InputSettings = []
            for item in params.get("InputSettings"):
                obj = InputSettingInfo()
                obj._deserialize(item)
                self.InputSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLiveInputResponse(AbstractModel):
    """ModifyStreamLiveInput response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyStreamLiveInputSecurityGroupRequest(AbstractModel):
    """ModifyStreamLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param Id: Input security group ID
        :type Id: str
        :param Name: Input security group name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param Whitelist: Allowlist entries (max: 10)
        :type Whitelist: list of str
        """
        self.Id = None
        self.Name = None
        self.Whitelist = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Whitelist = params.get("Whitelist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLiveInputSecurityGroupResponse(AbstractModel):
    """ModifyStreamLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OutputInfo(AbstractModel):
    """Output information.

    """

    def __init__(self):
        r"""
        :param Name: Output name.
        :type Name: str
        :param AudioTemplateNames: Audio transcoding template name array.
Quantity limit: [0,1] for RTMP; [0,20] for others.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AudioTemplateNames: list of str
        :param VideoTemplateNames: Video transcoding template name array. Quantity limit: [0,1].
Note: this field may return null, indicating that no valid values can be obtained.
        :type VideoTemplateNames: list of str
        :param Scte35Settings: SCTE-35 information configuration.
        :type Scte35Settings: :class:`tencentcloud.mdl.v20200326.models.Scte35SettingsInfo`
        :param AVTemplateNames: Audio/Video transcoding template name. If `HlsRemuxSettings.Scheme` is `MERGE`, there is 1 audio/video transcoding template. Otherwise, this parameter is empty.
Note: this field may return `null`, indicating that no valid value was found.
        :type AVTemplateNames: list of str
        """
        self.Name = None
        self.AudioTemplateNames = None
        self.VideoTemplateNames = None
        self.Scte35Settings = None
        self.AVTemplateNames = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.AudioTemplateNames = params.get("AudioTemplateNames")
        self.VideoTemplateNames = params.get("VideoTemplateNames")
        if params.get("Scte35Settings") is not None:
            self.Scte35Settings = Scte35SettingsInfo()
            self.Scte35Settings._deserialize(params.get("Scte35Settings"))
        self.AVTemplateNames = params.get("AVTemplateNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputsStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        r"""
        :param Pipeline0: Output information of pipeline 0.
        :type Pipeline0: list of PipelineOutputStatistics
        :param Pipeline1: Output information of pipeline 1.
        :type Pipeline1: list of PipelineOutputStatistics
        """
        self.Pipeline0 = None
        self.Pipeline1 = None


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self.Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = PipelineOutputStatistics()
                obj._deserialize(item)
                self.Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self.Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = PipelineOutputStatistics()
                obj._deserialize(item)
                self.Pipeline1.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PipelineInputStatistics(AbstractModel):
    """Pipeline input statistics.

    """

    def __init__(self):
        r"""
        :param Timestamp: Data timestamp in seconds.
        :type Timestamp: int
        :param NetworkIn: Input bandwidth in bps.
        :type NetworkIn: int
        :param Video: Video information array.
For `rtp/udp` input, the quantity is the number of `Pid` of the input video.
For other inputs, the quantity is 1.
        :type Video: list of VideoPipelineInputStatistics
        :param Audio: Audio information array.
For `rtp/udp` input, the quantity is the number of `Pid` of the input audio.
For other inputs, the quantity is 1.
        :type Audio: list of AudioPipelineInputStatistics
        """
        self.Timestamp = None
        self.NetworkIn = None
        self.Video = None
        self.Audio = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.NetworkIn = params.get("NetworkIn")
        if params.get("Video") is not None:
            self.Video = []
            for item in params.get("Video"):
                obj = VideoPipelineInputStatistics()
                obj._deserialize(item)
                self.Video.append(obj)
        if params.get("Audio") is not None:
            self.Audio = []
            for item in params.get("Audio"):
                obj = AudioPipelineInputStatistics()
                obj._deserialize(item)
                self.Audio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PipelineLogInfo(AbstractModel):
    """Pipeline log information.

    """

    def __init__(self):
        r"""
        :param Pipeline0: Log information of pipeline 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pipeline0: list of LogInfo
        :param Pipeline1: Log information of pipeline 1.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pipeline1: list of LogInfo
        """
        self.Pipeline0 = None
        self.Pipeline1 = None


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self.Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = LogInfo()
                obj._deserialize(item)
                self.Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self.Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = LogInfo()
                obj._deserialize(item)
                self.Pipeline1.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PipelineOutputStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        r"""
        :param Timestamp: Timestamp.
In seconds, indicating data time.
        :type Timestamp: int
        :param NetworkOut: Output bandwidth in bps.
        :type NetworkOut: int
        """
        self.Timestamp = None
        self.NetworkOut = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.NetworkOut = params.get("NetworkOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanReq(AbstractModel):
    """Event configuration information

    """

    def __init__(self):
        r"""
        :param EventName: Event name
        :type EventName: str
        :param TimingSettings: Event trigger time settings
        :type TimingSettings: :class:`tencentcloud.mdl.v20200326.models.TimingSettingsReq`
        :param EventSettings: Event configuration
        :type EventSettings: :class:`tencentcloud.mdl.v20200326.models.EventSettingsReq`
        """
        self.EventName = None
        self.TimingSettings = None
        self.EventSettings = None


    def _deserialize(self, params):
        self.EventName = params.get("EventName")
        if params.get("TimingSettings") is not None:
            self.TimingSettings = TimingSettingsReq()
            self.TimingSettings._deserialize(params.get("TimingSettings"))
        if params.get("EventSettings") is not None:
            self.EventSettings = EventSettingsReq()
            self.EventSettings._deserialize(params.get("EventSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanResp(AbstractModel):
    """Event configuration information

    """

    def __init__(self):
        r"""
        :param EventName: Event name
        :type EventName: str
        :param TimingSettings: Event trigger time settings
        :type TimingSettings: :class:`tencentcloud.mdl.v20200326.models.TimingSettingsResp`
        :param EventSettings: Event configuration
        :type EventSettings: :class:`tencentcloud.mdl.v20200326.models.EventSettingsResp`
        """
        self.EventName = None
        self.TimingSettings = None
        self.EventSettings = None


    def _deserialize(self, params):
        self.EventName = params.get("EventName")
        if params.get("TimingSettings") is not None:
            self.TimingSettings = TimingSettingsResp()
            self.TimingSettings._deserialize(params.get("TimingSettings"))
        if params.get("EventSettings") is not None:
            self.EventSettings = EventSettingsResp()
            self.EventSettings._deserialize(params.get("EventSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Scte35SettingsInfo(AbstractModel):
    """SCTE-35 configuration information.

    """

    def __init__(self):
        r"""
        :param Behavior: Whether to pass through SCTE-35 information. Valid values: NO_PASSTHROUGH/PASSTHROUGH. Default value: NO_PASSTHROUGH.
        :type Behavior: str
        """
        self.Behavior = None


    def _deserialize(self, params):
        self.Behavior = params.get("Behavior")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLiveChannelRequest(AbstractModel):
    """StartStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLiveChannelResponse(AbstractModel):
    """StartStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopStreamLiveChannelRequest(AbstractModel):
    """StopStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopStreamLiveChannelResponse(AbstractModel):
    """StopStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamAudioInfo(AbstractModel):
    """Audio information.

    """

    def __init__(self):
        r"""
        :param Pid: Audio `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pid: int
        :param Codec: Audio codec.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Codec: str
        :param Fps: Audio frame rate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Fps: int
        :param Rate: Audio bitrate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rate: int
        :param SampleRate: Audio sample rate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SampleRate: int
        """
        self.Pid = None
        self.Codec = None
        self.Fps = None
        self.Rate = None
        self.SampleRate = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.SampleRate = params.get("SampleRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamInfo(AbstractModel):
    """Push information.

    """

    def __init__(self):
        r"""
        :param ClientIp: Client IP.
        :type ClientIp: str
        :param Video: Video information of pushed streams.
        :type Video: list of StreamVideoInfo
        :param Audio: Audio information of pushed streams.
        :type Audio: list of StreamAudioInfo
        :param Scte35: SCTE-35 information of pushed streams.
        :type Scte35: list of StreamScte35Info
        """
        self.ClientIp = None
        self.Video = None
        self.Audio = None
        self.Scte35 = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        if params.get("Video") is not None:
            self.Video = []
            for item in params.get("Video"):
                obj = StreamVideoInfo()
                obj._deserialize(item)
                self.Video.append(obj)
        if params.get("Audio") is not None:
            self.Audio = []
            for item in params.get("Audio"):
                obj = StreamAudioInfo()
                obj._deserialize(item)
                self.Audio.append(obj)
        if params.get("Scte35") is not None:
            self.Scte35 = []
            for item in params.get("Scte35"):
                obj = StreamScte35Info()
                obj._deserialize(item)
                self.Scte35.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamLiveChannelInfo(AbstractModel):
    """Channel information

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        :param State: Channel status
        :type State: str
        :param AttachedInputs: Information of attached inputs
        :type AttachedInputs: list of AttachedInput
        :param OutputGroups: Information of output groups
        :type OutputGroups: list of StreamLiveOutputGroupsInfo
        :param Name: Channel name
        :type Name: str
        :param AudioTemplates: Audio transcoding templates
Note: this field may return `null`, indicating that no valid value was found.
        :type AudioTemplates: list of AudioTemplateInfo
        :param VideoTemplates: Video transcoding templates
Note: this field may return `null`, indicating that no valid value was found.
        :type VideoTemplates: list of VideoTemplateInfo
        :param AVTemplates: Audio/Video transcoding templates
Note: this field may return `null`, indicating that no valid value was found.
        :type AVTemplates: list of AVTemplate
        """
        self.Id = None
        self.State = None
        self.AttachedInputs = None
        self.OutputGroups = None
        self.Name = None
        self.AudioTemplates = None
        self.VideoTemplates = None
        self.AVTemplates = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.State = params.get("State")
        if params.get("AttachedInputs") is not None:
            self.AttachedInputs = []
            for item in params.get("AttachedInputs"):
                obj = AttachedInput()
                obj._deserialize(item)
                self.AttachedInputs.append(obj)
        if params.get("OutputGroups") is not None:
            self.OutputGroups = []
            for item in params.get("OutputGroups"):
                obj = StreamLiveOutputGroupsInfo()
                obj._deserialize(item)
                self.OutputGroups.append(obj)
        self.Name = params.get("Name")
        if params.get("AudioTemplates") is not None:
            self.AudioTemplates = []
            for item in params.get("AudioTemplates"):
                obj = AudioTemplateInfo()
                obj._deserialize(item)
                self.AudioTemplates.append(obj)
        if params.get("VideoTemplates") is not None:
            self.VideoTemplates = []
            for item in params.get("VideoTemplates"):
                obj = VideoTemplateInfo()
                obj._deserialize(item)
                self.VideoTemplates.append(obj)
        if params.get("AVTemplates") is not None:
            self.AVTemplates = []
            for item in params.get("AVTemplates"):
                obj = AVTemplate()
                obj._deserialize(item)
                self.AVTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamLiveOutputGroupsInfo(AbstractModel):
    """Channel output group information

    """

    def __init__(self):
        r"""
        :param Name: Output group name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the channel level
        :type Name: str
        :param Type: Output protocol
Valid values: `HLS`, `DASH`, `HLS_ARCHIVE`, `HLS_STREAM_PACKAGE`, `DASH_STREAM_PACKAGE`
        :type Type: str
        :param Outputs: Output information
If the type is RTMP or RTP, only one output is allowed; if it is HLS or DASH, 1-10 outputs are allowed.
        :type Outputs: list of OutputInfo
        :param Destinations: Relay destinations. Quantity: [1, 2]
        :type Destinations: list of DestinationInfo
        :param HlsRemuxSettings: HLS protocol configuration information, which takes effect only for HLS/HLS_ARCHIVE outputs
Note: this field may return `null`, indicating that no valid value was found.
        :type HlsRemuxSettings: :class:`tencentcloud.mdl.v20200326.models.HlsRemuxSettingsInfo`
        :param DrmSettings: DRM configuration information
Note: this field may return `null`, indicating that no valid value was found.
        :type DrmSettings: :class:`tencentcloud.mdl.v20200326.models.DrmSettingsInfo`
        :param DashRemuxSettings: DASH protocol configuration information, which takes effect only for DASH/DASH_ARCHIVE outputs
Note: this field may return `null`, indicating that no valid value was found.
        :type DashRemuxSettings: :class:`tencentcloud.mdl.v20200326.models.DashRemuxSettingsInfo`
        :param StreamPackageSettings: StreamPackage configuration information, which is required if the output type is StreamPackage
Note: this field may return `null`, indicating that no valid value was found.
        :type StreamPackageSettings: :class:`tencentcloud.mdl.v20200326.models.StreamPackageSettingsInfo`
        """
        self.Name = None
        self.Type = None
        self.Outputs = None
        self.Destinations = None
        self.HlsRemuxSettings = None
        self.DrmSettings = None
        self.DashRemuxSettings = None
        self.StreamPackageSettings = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        if params.get("Outputs") is not None:
            self.Outputs = []
            for item in params.get("Outputs"):
                obj = OutputInfo()
                obj._deserialize(item)
                self.Outputs.append(obj)
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = DestinationInfo()
                obj._deserialize(item)
                self.Destinations.append(obj)
        if params.get("HlsRemuxSettings") is not None:
            self.HlsRemuxSettings = HlsRemuxSettingsInfo()
            self.HlsRemuxSettings._deserialize(params.get("HlsRemuxSettings"))
        if params.get("DrmSettings") is not None:
            self.DrmSettings = DrmSettingsInfo()
            self.DrmSettings._deserialize(params.get("DrmSettings"))
        if params.get("DashRemuxSettings") is not None:
            self.DashRemuxSettings = DashRemuxSettingsInfo()
            self.DashRemuxSettings._deserialize(params.get("DashRemuxSettings"))
        if params.get("StreamPackageSettings") is not None:
            self.StreamPackageSettings = StreamPackageSettingsInfo()
            self.StreamPackageSettings._deserialize(params.get("StreamPackageSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamPackageSettingsInfo(AbstractModel):
    """StreamPackage settings when the output type is StreamPackage

    """

    def __init__(self):
        r"""
        :param Id: Channel ID in StreamPackage
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamScte35Info(AbstractModel):
    """SCTE-35 information.

    """

    def __init__(self):
        r"""
        :param Pid: SCTE-35 `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pid: int
        """
        self.Pid = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamVideoInfo(AbstractModel):
    """Video information of pushed streams.

    """

    def __init__(self):
        r"""
        :param Pid: Video `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pid: int
        :param Codec: Video codec.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Codec: str
        :param Fps: Video frame rate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Fps: int
        :param Rate: Video bitrate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rate: int
        :param Width: Video width.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Width: int
        :param Height: Video height.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Height: int
        """
        self.Pid = None
        self.Codec = None
        self.Fps = None
        self.Rate = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingSettingsReq(AbstractModel):
    """Event trigger time settings

    """

    def __init__(self):
        r"""
        :param StartType: Event trigger type. Valid values: `FIXED_TIME`, `IMMEDIATE`
        :type StartType: str
        :param Time: Required if `StartType` is `FIXED_TIME`
UTC time, such as `2020-01-01T12:00:00Z`
        :type Time: str
        """
        self.StartType = None
        self.Time = None


    def _deserialize(self, params):
        self.StartType = params.get("StartType")
        self.Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingSettingsResp(AbstractModel):
    """Event trigger time settings

    """

    def __init__(self):
        r"""
        :param StartType: Event trigger type
        :type StartType: str
        :param Time: Not empty if `StartType` is `FIXED_TIME`
UTC time, such as `2020-01-01T12:00:00Z`
        :type Time: str
        """
        self.StartType = None
        self.Time = None


    def _deserialize(self, params):
        self.StartType = params.get("StartType")
        self.Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoPipelineInputStatistics(AbstractModel):
    """Pipeline input video statistics.

    """

    def __init__(self):
        r"""
        :param Fps: Video FPS.
        :type Fps: int
        :param Rate: Video bitrate in bps.
        :type Rate: int
        :param Pid: Video `Pid`, which is available only if the input is `rtp/udp`.
        :type Pid: int
        """
        self.Fps = None
        self.Rate = None
        self.Pid = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTemplateInfo(AbstractModel):
    """Video transcoding template.

    """

    def __init__(self):
        r"""
        :param Name: Video transcoding template name, which can contain 1-20 letters and digits.
        :type Name: str
        :param Vcodec: Video codec. Valid values: H264/H265. If this parameter is left empty, the original value will be used.
        :type Vcodec: str
        :param VideoBitrate: Video bitrate. Value range: [50000,40000000]. The value can only be a multiple of 1,000. If this parameter is left empty, the original value will be used.
        :type VideoBitrate: int
        :param Width: Video width. Value range: (0,3000]. The value can only be a multiple of 4. If this parameter is left empty, the original value will be used.
        :type Width: int
        :param Height: Video height. Value range: (0,3000]. The value can only be a multiple of 4. If this parameter is left empty, the original value will be used.
        :type Height: int
        :param Fps: Video frame rate. Value range: [1,240]. If this parameter is left empty, the original value will be used.
        :type Fps: int
        :param TopSpeed: Whether to enable top speed codec. Valid value: CLOSE/OPEN. Default value: CLOSE.
        :type TopSpeed: str
        :param BitrateCompressionRatio: Top speed codec compression ratio. Value range: [0,50]. The lower the compression ratio, the higher the image quality.
        :type BitrateCompressionRatio: int
        :param RateControlMode: Bitrate control mode. Valid values: `CBR`, `ABR` (default)
        :type RateControlMode: str
        """
        self.Name = None
        self.Vcodec = None
        self.VideoBitrate = None
        self.Width = None
        self.Height = None
        self.Fps = None
        self.TopSpeed = None
        self.BitrateCompressionRatio = None
        self.RateControlMode = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Vcodec = params.get("Vcodec")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.TopSpeed = params.get("TopSpeed")
        self.BitrateCompressionRatio = params.get("BitrateCompressionRatio")
        self.RateControlMode = params.get("RateControlMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        