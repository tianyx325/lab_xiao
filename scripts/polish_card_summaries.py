# -*- coding: utf-8 -*-
"""Polish non-member card summaries to ~2–3 lines (about 50–80 Chinese chars)."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / "content"

# key = relative path under content/, value = summary text
SUMMARIES: dict[str, str] = {
    # publications
    "publication/cedflow-aaai-2024": (
        "面向暗光与低信噪比场景的光流估计，提出隐空间轮廓增强方法 CEDFlow，"
        "在保持运动一致性的同时提升弱光条件下的光流精度与稳定性。"
    ),
    "publication/cjig-2024-siamese-lowlight": (
        "针对弱光条件下光流易退化问题，构建隐特征监督的孪生网络，"
        "在低照度视频上实现更稳健的运动估计与特征对齐。"
    ),
    "publication/cvpr-2014-aliasing": (
        "围绕全光场成像中的混叠伪影，研究检测与抑制方法，"
        "改善重聚焦与视点合成中的成像质量与细节保真度。"
    ),
    "publication/tip-2022-fdl-hcgh": (
        "在尺度—视差空间中设计光场 FDL-HCGH 特征，"
        "增强光场数据的可区分性，支撑匹配、检索等下游视觉任务。"
    ),
    # awards
    "award/china-boguan-2026": (
        "高校文旅大模型《易见博观·智绘万象》完成自主研发与教学实践落地，"
        "获全国高校网络文化技术创新大会自主研发应用二等奖。"
    ),
    "award/china-invention-association-2023": (
        "围绕复杂场景可视数据语义分析关键技术开展研究与应用转化，"
        "获中国发明协会创新创业奖二等奖（排名第二）。"
    ),
    "award/shaanxi-cs-invention-2021": (
        "面向视频监控场景，突破可视计算关键技术并推进工程应用，"
        "获陕西省计算机学会技术发明一等奖（排名第二）。"
    ),
    "award/shaanxi-tech-invention-2025": (
        "针对复杂场景视频语义分析与理解开展系统研究与应用示范，"
        "获陕西省技术发明奖二等奖（排名第三）。"
    ),
    # research directions
    "research/action": (
        "面向人体行为理解，研究基于骨骼点与视觉特征的动作识别方法，"
        "覆盖时空建模、鲁棒表征及真实场景下的行为理解应用。"
    ),
    "research/agent": (
        "面向大语言模型与智能体，研究任务规划、工具调用与多智能体协作，"
        "推动垂直场景中的应用落地、评测与决策能力提升。"
    ),
    "research/depth": (
        "面向常规与降质场景，研究单目、弱光及事件相机条件下的深度估计，"
        "探索语义引导、多模态融合与鲁棒三维感知方法。"
    ),
    "research/low-light": (
        "面向低照度与复杂光照，研究图像/视频增强、去噪与特征表达，"
        "提升下游对焦、匹配与重建等任务在弱光条件下的可用性。"
    ),
    # post
    "post/2026-welcome": (
        "欢迎 2026 级同学加入智能感知与决策实验室。"
        "实验室专注弱光视觉、深度估计、动作识别与智能体等方向，期待共同成长。"
    ),
    # projects
    "project/bao-zha-chang-bian-ma-zhao-ming-xi-tong-zhuang-zhi-ji-biao-d": (
        "面向爆炸场观测需求，研制编码照明系统装置并完成标定方法研究，"
        "提升极端环境下成像可控性与测量可靠性。"
    ),
    "project/duo-yuan-guang-chang-cheng-xiang-xi-tong-biao-ding-fang-fa": (
        "研究多源光场成像系统的联合标定方法，"
        "提高跨设备、跨模态光场数据的几何一致性与后续计算精度。"
    ),
    "project/guang-chang-te-zheng-ti-qu-yu-ying-yong-fang-fa-yan-jiu": (
        "研究光场数据的特征提取与表示方法，"
        "并探索其在匹配、识别等计算机视觉任务中的应用路径。"
    ),
    "project/guang-fu-mian-ban-hong-wai-cheng-xiang-de-re-ban-que-xian-ji": (
        "基于光伏面板红外成像，开发热斑缺陷自动检测算法，"
        "支撑巡检场景下的高效缺陷识别与质量控制。"
    ),
    "project/hai-sheng-cheng-xiang-shu-ju-chu-li-ji-mu-biao-jian-ce-fang": (
        "面向海声成像数据，研究预处理与目标检测方法，"
        "提升复杂水声环境中的目标可检测性与判读效率。"
    ),
    "project/ji-dong-che-xing-shi-zheng-dian-zi-cuan-gai-jian-ce-suan-fa": (
        "针对机动车行驶证电子图像，开发篡改检测算法，"
        "识别常见伪造痕迹，服务证件核验与安全监管。"
    ),
    "project/jia-ju-shi-gong-gong-cheng-xie-tong-guan-li-kong-zhi-ruan-ji": (
        "研制家具施工工程协同管理控制软件，"
        "打通进度、质量与现场协同流程，提升工程信息化管理水平。"
    ),
    "project/proj-2016jq6069": (
        "研究光场深度估计及其优化方法，"
        "提升复杂场景下深度重建精度，服务三维感知与计算成像应用。"
    ),
    "project/proj-2019jm-221": (
        "面向宽基线光场数据，研究特征提取与紧凑表示方法，"
        "增强跨视点匹配稳定性与后续视觉任务性能。"
    ),
    "project/proj-61501370": (
        "研究光场成像轴向超分辨率方法，"
        "突破光学系统轴向分辨限制，改善重聚焦与三维细节恢复能力。"
    ),
    "project/proj-61871319": (
        "研究双平面光场局部不变性特征的提取与匹配，"
        "提升光场数据在变化视角与尺度条件下的对应可靠性。"
    ),
    "project/proj-62031023": (
        "面向高分辨率动态光场，研究获取装置与计算理论方法，"
        "支撑动态场景的光场采集、重建与高质量可视化。"
    ),
    "project/proj-62371389": (
        "面向弱光自动对焦，研究光场特征计算与增强理论方法，"
        "提升低照度条件下对焦稳定性与成像可用性。"
    ),
    "project/proj-buaa-vr-16kf-10": (
        "围绕光场成像链路开展优化方法研究，"
        "改进采集与重建质量，服务虚拟现实等相关应用需求。"
    ),
    "project/ruo-guang-tu-xiang-zeng-qiang-suan-fa-ding-zhi-kai-fa": (
        "面向实际业务场景定制弱光图像增强算法，"
        "在低照度条件下恢复可见细节，提升后续识别与分析效果。"
    ),
    "project/xiang-ji-zhen-lie-guang-chang-cai-ji-ji-zi-you-shi-dian-guan": (
        "基于相机阵列开展光场采集，并研究自由视点重建方法，"
        "实现多视角光场数据的高质量合成与漫游展示。"
    ),
}

# Patents: keep domain cue + expand to 2 clauses (~55–75 chars)
PATENT_SUMMARIES: dict[str, str] = {
    "patent/zl-2010102577956": (
        "面向虚拟现实与图像处理需求，提出高分辨率实时全景高动态范围图像获取装置与方法，"
        "实现 360° 全景数字图像的高效采集与合成。"
    ),
    "patent/zl-2014106961638": (
        "面向计算机视觉与光学工程，提出可变角度采样数的光场采集装置，"
        "在灵活采样配置下获取更高质量的光场数据。"
    ),
    "patent/zl-2016104162235": (
        "面向光场成像设备性能评价，提出轴向分辨率测定装置与方法，"
        "适用于双平面等光场系统的参数标定与指标量化。"
    ),
    "patent/zl-2016104163793": (
        "面向计算摄像与光学工程，提出高角度分辨率光场获取装置及图像生成方法，"
        "提升角度维信息采集能力与成像表现。"
    ),
    "patent/zl-2016105703924": (
        "面向数字成像与光学应用，提出三维表面光场编码生成及识别装置与方法，"
        "支撑结构化光场编码信号的生成、采集与识别。"
    ),
    "patent/zl-2016108247124": (
        "面向多视计算机视觉，提出基于水平集函数演化的非刚性目标场景流估计方法，"
        "提升复杂形变场景下的运动与结构估计能力。"
    ),
    "patent/zl-2018104477624": (
        "面向水声信号处理，提出基于高斯混合模型的宽吻海豚 click 信号检测方法，"
        "提高复杂噪声背景下生物声信号的检出可靠性。"
    ),
    "patent/zl-2018104563418": (
        "面向视频理解与摘要生成，提出基于超像素分割的视频摘要方法，"
        "在保留关键内容的同时压缩冗余镜头信息。"
    ),
    "patent/zl-2018104727899": (
        "面向实验动物行为分析，提出小鼠视频多维特征值提取及分类方法，"
        "支撑行为量化评估与自动视频分类。"
    ),
    "patent/zl-2019106504175": (
        "面向光场轴向成像，提出基于生成对抗网络的光场图像轴向超分辨方法，"
        "改善重聚焦结果的细节清晰度与观感质量。"
    ),
    "patent/zl-2019107640228": (
        "面向光场超分辨重建，提出基于 EPI 的光场图像超分辨方法，"
        "利用极线图像结构提升空间分辨率与边缘保真。"
    ),
    "patent/zl-2020104527245": (
        "面向电力巡检，提出绝缘子缺损自动检测算法，"
        "在巡检视频中定位典型缺损，提高巡检效率与一致性。"
    ),
    "patent/zl-2021103397944": (
        "面向特征匹配可靠性，提出基于孪生卷积网络与特征混合的 SIFT 误匹配检测方法，"
        "降低错误对应关系对后续几何估计的影响。"
    ),
    "patent/zl-2021103812222": (
        "面向证件图像安全，提出光场防篡改采集装置及方法，"
        "利用光场信息增强证件数字图像的防伪与溯源能力。"
    ),
    "patent/zl-2021103833727": (
        "面向光场特征提取，提出基于角度域变化矩阵的特征点检测方法，"
        "提升光场数据中稳定特征点的定位能力。"
    ),
    "patent/zl-2021106394882": (
        "面向光伏运维，提出基于 Yolo-v4 的面板暗斑缺陷检测方法，"
        "实现红外/可见巡检图像中暗斑目标的自动识别。"
    ),
    "patent/zl-2021116140810": (
        "面向特征匹配纠错，提出结合图像语义与坐标关系的误匹配检测方法，"
        "融合语义与几何约束筛选不可靠对应点。"
    ),
    "patent/zl-2023109720647": (
        "面向人脸分析，提出基于 Transformer 的双分支人脸关键点检测方法，"
        "提升复杂姿态与光照条件下的关键点定位精度。"
    ),
    "patent/zl-2023110395016": (
        "面向多聚焦成像，提出基于光场重聚焦特征学习的图像融合方法，"
        "在保留清晰区域的同时抑制虚焦与伪影。"
    ),
}


def set_summary(fm: str, summary: str) -> str:
    q = summary.replace('"', '\\"')
    if re.search(r"^summary:\s*", fm, re.M):
        fm, n = re.subn(
            r"^summary:\s*[^\n]*$",
            f'summary: "{q}"',
            fm,
            count=1,
            flags=re.M,
        )
        if n != 1:
            raise SystemExit("summary replace failed")
        return fm
    # insert after title
    if re.search(r"^title:\s*.+$", fm, re.M):
        return re.sub(
            r"^(title:\s*.+)$",
            rf'\1\nsummary: "{q}"',
            fm,
            count=1,
            flags=re.M,
        )
    return f'summary: "{q}"\n' + fm


def main() -> None:
    all_map = {**SUMMARIES, **PATENT_SUMMARIES}
    for rel, summary in sorted(all_map.items()):
        f = ROOT / rel / "index.md"
        if not f.exists():
            raise SystemExit(f"missing: {f}")
        text = f.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) < 3:
            raise SystemExit(f"bad fm: {f}")
        fm = set_summary(parts[1], summary)
        f.write_text(f"---{fm}---{parts[2]}", encoding="utf-8", newline="\n")
        print(f"OK {rel} ({len(summary)} chars)")


if __name__ == "__main__":
    main()
