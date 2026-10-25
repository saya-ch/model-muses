# Model Muses

> 22 AI models & platforms · original illustrations · technical profiles · official links · per-image provenance

本仓库收录 22 个主流大模型与 AI 工具的拟人形象立绘原画。全部图片出自**同一位画师、同一批次、同一画风**的白底全身立绘，规格统一，可横向对比。

下表「本体说明」讲的是**每个对象本身的技术定位**——它属于哪一类技术、采用什么架构机制、在什么方向上有独特性。为保持表格可读，此处只列核心机制；更完整的对照见 [docs/角色设定与设计规律.md](docs/角色设定与设计规律.md)。

<table>
<tr>
<td width="170"><b>DeepSeek</b><br><a href="https://www.deepseek.com/">官网</a> · <a href="https://api-docs.deepseek.com/">API 文档</a> · <a href="https://github.com/deepseek-ai">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/deepseek.jpg" width="120"></td>
<td>DeepSeek（深度求索）背后是量化投资公司幻方量化，其模型走稀疏 MoE 路线。核心是 <b>MLA</b>——把 KV cache 压进低秩潜空间，显存占用远低于标准多头注意力。配<b>细粒度专家切分</b>、<b>无辅助损失的负载均衡</b>与<b>多 token 预测</b>训练目标。推理线用 <b>GRPO</b> 直接对基座做强化学习，不经人工思维链标注即自发产生长链推理；最新一代已从纯文本扩展到<b>原生多模态视觉理解</b>。权重与代码以 MIT 协议开放，明确允许蒸馏与商用。</td>
</tr>
<tr>
<td width="170"><b>GPT（OpenAI）</b><br><a href="https://openai.com/">官网</a> · <a href="https://platform.openai.com/docs">开发者文档</a> · <a href="https://github.com/openai">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/gpt.jpg" width="120"></td>
<td>GPT 来自 OpenAI，是闭源前沿通用模型的代表。真正的护城河在<b>工具调用协议与生态集成</b>——结构化接口稳定驱动外部工具，长流程不易崩格式，第三方 Agent 框架的适配面最大；近年重心进一步转向<b>可执行的编程代理</b>形态，把推理直接落成对仓库与环境的操作。闭源，不可自部署。</td>
</tr>
<tr>
<td width="170"><b>Claude（Anthropic）</b><br><a href="https://www.anthropic.com/">官网</a> · <a href="https://docs.claude.com/">文档</a> · <a href="https://github.com/anthropics">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/claude.jpg" width="120"></td>
<td>Claude 出自 Anthropic，主打<b>长程智能体可靠性与代码能力</b>。四个关键机制：<b>可调推理强度</b>（effort 分四档，无需更换模型即可切换快慢）、<b>自适应思考</b>（由模型自行判断何时需要深度推理）、<b>上下文压缩</b>（接近阈值时服务端自动摘要旧上下文）、以及<b>提示缓存</b>（复用历史前缀，Agent 循环不重复付费）。Agent 侧已从单代理走向<b>多代理协作</b>。</td>
</tr>
<tr>
<td width="170"><b>Gemini（Google）</b><br><a href="https://deepmind.google/models/gemini/">模型页</a> · <a href="https://ai.google.dev/gemini-api/docs">API 文档</a> · <a href="https://github.com/google-deepmind">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/gemini.jpg" width="120"></td>
<td>Gemini 出自 Google DeepMind，是唯一以<b>原生多模态</b>为核心的全栈模型：单模型同时处理文本、图像、音频、视频、PDF 与代码，无需外挂专用模型拼接。推理深度可按档位调节；与 Google 搜索、地图等第一方服务<b>原生打通</b>，可直接注入已验证的检索结果。</td>
</tr>
<tr>
<td width="170"><b>Grok（xAI）</b><br><a href="https://x.ai/">官网</a> · <a href="https://docs.x.ai/">API 文档</a> · <a href="https://github.com/xai-org">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/grok.jpg" width="120"></td>
<td>Grok 来自马斯克的 xAI，是通用对话与推理模型。差异点是<b>实时性</b>——检索层直接接 X 平台的数据流，DeepSearch 一类能力会读取当下社交帖子与突发新闻，而非依赖训练截止的静态知识。输出侧已能<b>原生生成演示文稿、PDF 与表格</b>；代价是来源缺少权威性筛选。风格与安全策略一贯偏开放。</td>
</tr>
<tr>
<td width="170"><b>Kimi（月之暗面）</b><br><a href="https://www.moonshot.cn/">官网</a> · <a href="https://platform.moonshot.cn/">开放平台</a> · <a href="https://github.com/MoonshotAI">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/kimi.jpg" width="120"></td>
<td>Kimi 来自月之暗面（Moonshot AI），走 MoE 路线，自研 <b>Kimi Delta Attention</b> 混合线性注意力与<b>注意力残差</b>，配合量化感知训练直接产出低比特权重，支撑起百万级上下文。模型系列本身即 <b>agentic</b>，接上工具能自主完成多步任务。推理侧为<b>混合思考模式</b>。开放权重，采用带附加条件的开放许可。</td>
</tr>
<tr>
<td width="170"><b>Qwen（通义千问）</b><br><a href="https://qwenlm.github.io/">官网</a> · <a href="https://github.com/QwenLM">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/qwen.jpg" width="120"></td>
<td>Qwen（通义千问）是阿里云通义团队的开源模型系列，<b>覆盖最全的一条产品线</b>：轻量稠密到大规模 MoE，端侧到企业级。技术亮点是<b>混合思考模式</b>（开关切换分步推理与快速响应，配思考预算控成本）、多语言支持、统一多模态编码与<b>原生 MCP</b>。全系 Apache 2.0，商用无限制。</td>
</tr>
<tr>
<td width="170"><b>GLM（智谱）</b><br><a href="https://docs.bigmodel.cn/">开放文档</a> · <a href="https://github.com/THUDM">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/glm.jpg" width="120"></td>
<td>GLM 出自智谱（Zhipu AI，源自清华知识工程实验室），采用 MoE 架构。<b>参数效率</b>是核心卖点——轻量版本可比肩更大的闭源模型。<b>混合推理模式</b>可切，针对工具调用、网页浏览与软件工程做了专门优化；另有<b>原生多模态分支</b>，与 OCR、语音、图像生成等细分模型构成全模态矩阵。权重以 MIT 协议开放。</td>
</tr>
<tr>
<td width="170"><b>混元（腾讯）</b><br><a href="https://github.com/Tencent-Hunyuan">GitHub</a> · <a href="https://hunyuan.tencent.com/">混元官网</a></td>
<td width="130" align="center"><img src="原画/thumbs/hunyuan.jpg" width="120"></td>
<td>混元是腾讯自研的大模型系列，走<b>中文语料加全模态</b>路线，文本、图像、语音、视频与 3D 生成并行推进。深度依托腾讯云与微信生态，针对中文语境与本土知识优化。开源版本覆盖语言、<b>视频世界模型</b>与 <b>3D 重建</b>方向：前者按片段生成、过程中可用文字介入改写场景，后者能在单张消费级显卡上秒级重建 3D 世界。多个项目以 Apache 2.0 协议发布。</td>
</tr>
<tr>
<td width="170"><b>豆包 Seed（字节跳动）</b><br><a href="https://seed.bytedance.com/">Seed 官网</a> · <a href="https://www.volcengine.com/docs/ark">火山方舟文档</a> · <a href="https://github.com/volcengine">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/seed.jpg" width="120"></td>
<td>豆包 Seed 是字节跳动 Seed 团队的模型系列，经火山引擎对外提供服务，主线是<b>统一多模态架构</b>——单主干同时接收文本、图像、视频、音频并做跨模态联合推理，而非拼接多个专用模型。工程重点在视觉编码器瘦身与长上下文访存成本。产品侧另有一条<b>按周迭代的动态模型</b>，以统一模型 ID 持续推送最新版本；生成侧另有图像、视频、语音与 3D 资产的独立模型线。</td>
</tr>
<tr>
<td width="170"><b>Llama（Meta）</b><br><a href="https://llama.meta.com/">官网</a> · <a href="https://huggingface.co/meta-llama">模型页</a></td>
<td width="130" align="center"><img src="原画/thumbs/llama.jpg" width="120"></td>
<td>Llama 来自 Meta，是<b>开放权重路线</b>的代表：权重公开，衍生出大量微调版与量化版，主导私有化部署与学术复现生态，最新一代采用<b>早期融合的原生多模态 MoE</b> 设计。它同时是别人的底座——多个主流产品以其为基座后训练。授权为社区许可：可商用，但须标注「Built with Llama」、衍生模型名以 Llama 开头，且超出月活阈值的大平台需单独取得授权。</td>
</tr>
<tr>
<td width="170"><b>Mistral AI</b><br><a href="https://mistral.ai/">官网</a> · <a href="https://docs.mistral.ai/">文档</a> · <a href="https://github.com/mistralai">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/mistral.jpg" width="120"></td>
<td>Mistral AI 是一家总部位于巴黎的欧洲厂商，以<b>高效小模型与开放权重</b>著称：参数压得比同档更狠而质量不降，小尺寸系列广泛用于端侧与边缘部署，另有稀疏 MoE 版与长文档结构化输出模型。授权分层明确——多数开源模型用 Apache 2.0，部分走改版 MIT（月营收超阈值需转商业授权），旗舰模型则提供非商用免费与商业授权两条路。另有 OCR、语音等周边模型。</td>
</tr>
<tr>
<td width="170"><b>MiniMax</b><br><a href="https://www.minimax.io/">官网</a> · <a href="https://platform.minimax.io/docs">平台文档</a> · <a href="https://github.com/MiniMax-AI">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/minimax.jpg" width="120"></td>
<td>MiniMax（稀宇科技）是上海的基础模型公司，本体是<b>全模态自研底座</b>：文本、语音、视频、音乐全部自研而非集成他人。工程路线上以自研<b>线性注意力</b>打破注意力复杂度带来的上下文长度限制，后续转向稀疏注意力架构。生成侧已做到<b>单模型同时输出带原生立体声的高分辨率视频</b>——对白、音效与环境声在同一次生成中完成，靠自研的高压缩 tokenizer 降低生成开销，并开放了权重供本地部署。</td>
</tr>
<tr>
<td width="170"><b>Perplexity</b><br><a href="https://www.perplexity.ai/">官网</a> · <a href="https://docs.perplexity.ai/">API 文档</a> · <a href="https://github.com/perplexityai">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/perplexity.jpg" width="120"></td>
<td>Perplexity 出自 Perplexity AI，本质是<b>检索增强生成（RAG）引擎</b>，而非参数化知识模型——每次回答都必须经过实时检索。核心资产是自建的实时网页索引，由预索引与实时抓取两套爬虫持续更新，索引层跑在 Vespa 之上；检索层混合自建索引与外部搜索 API，经相关性与权威性等多道关卡筛选后综合成带内联引用的回答。综合层使用自研 Sonar 系列（基于 Llama 后训练），并路由多家前沿闭源模型处理更难的查询；之上是能多步检索并交叉核验的深度研究模式。</td>
</tr>
<tr>
<td width="170"><b>GitHub</b><br><a href="https://github.com/">官网</a> · <a href="https://docs.github.com/en/copilot">Copilot 文档</a></td>
<td width="130" align="center"><img src="原画/thumbs/github.jpg" width="120"></td>
<td>GitHub 是微软旗下的代码托管平台，<b>本体是协作基础设施而非 AI 模型</b>。对 AI 时代的影响在两条线：<b>Copilot</b> 已从编辑器补全扩展成终端里的完整 agentic 开发环境——具备计划模式与<b>自动驾驶模式</b>、内置专用子代理、并行执行与后台委派，并支持 MCP、插件、Agent Skills 与自定义 agent；此外把主流模型接入自家 Agent 与云端开发环境，直接作用于仓库、PR、Issue 与 CI。</td>
</tr>
<tr>
<td width="170"><b>GitLab</b><br><a href="https://about.gitlab.com/">官网</a> · <a href="https://docs.gitlab.com/">文档</a></td>
<td width="130" align="center"><img src="原画/thumbs/gitlab.jpg" width="120"></td>
<td>GitLab 出自 GitLab Inc.，以 <b>DevSecOps 全生命周期</b>为定位：代码托管、CI/CD、制品管理、安全扫描、容器注册表一站式覆盖。AI 侧是 <b>GitLab Duo Agent Platform</b>——把补全、代码解释、漏洞检测与 MR 评审嵌进流水线，并作为 MCP 客户端接入外部系统；差异在于<b>把 AI 放进 DevSecOps 的每个环节</b>。有 SaaS 与自托管开源版。</td>
</tr>
<tr>
<td width="170"><b>Gitee（码云）</b><br><a href="https://gitee.com/">官网</a></td>
<td width="130" align="center"><img src="原画/thumbs/gitee.jpg" width="120"></td>
<td>Gitee（码云）由开源中国（OSCHINA）推出，是国内的代码托管平台，重心在<b>国产化适配</b>：支持信创软硬件环境、代码安全合规扫描、对接企业内部研发系统。AI 侧提供补全与对话式助手，并配套自有的模型分发平台，可对接国产大模型以满足私有化与数据不出域。</td>
</tr>
<tr>
<td width="170"><b>Hugging Face</b><br><a href="https://huggingface.co/">官网</a> · <a href="https://huggingface.co/docs/transformers/index">transformers 文档</a></td>
<td width="130" align="center"><img src="原画/thumbs/huggingface.jpg" width="120"></td>
<td>Hugging Face 是同名公司运营的<b>模型托管与分发平台</b>，不是模型本身。核心是 Hub（模型/数据集/应用的托管与版本管理），配套的 <b>transformers</b> 库已成为开源模型加载的事实标准抽象层。该平台 2026 年 9 月与英伟达达成约 129 亿美元收购协议，官方承诺继续作为开放平台独立运营、不强制绑定自家算力。</td>
</tr>
<tr>
<td width="170"><b>RWKV</b><br><a href="https://wiki.rwkv.com/">官方 Wiki</a> · <a href="https://rwkv.cn/">中文站</a> · <a href="https://github.com/RWKV">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/rwkv.jpg" width="120"></td>
<td>RWKV 由彭博（Bo Peng）提出，2023 年并入 Linux 基金会，现为其下的开源非营利项目，是一种<b>非 Transformer 架构</b>的线性注意力语言模型。原理是把 softmax 点积注意力改写为线性递推：训练时并行展开，推理时退化为 RNN——<b>显存与生成速度恒定、完全不需要 KV cache</b>。第七代架构引入动态状态演化，突破了注意力范式的表达力上限。代价是失去任意回看任意 token 的能力，长文精确回忆偏弱。权重 Apache 2.0。</td>
</tr>
<tr>
<td width="170"><b>OpenCode</b><br><a href="https://opencode.ai/">官网</a> · <a href="https://github.com/anomalyco/opencode">GitHub</a></td>
<td width="130" align="center"><img src="原画/thumbs/opencode.jpg" width="120"></td>
<td>OpenCode 由 Anomaly（原 SST）开源，本体是<b>与模型解耦的 AI 编码 agent 外壳</b>：终端、桌面、Web、IDE 扩展多形态，底层经 <b>Models.dev</b> 接入数十家供应商，也可直连各家订阅账户。早期版本原生加载语言服务器取精确符号与诊断，后续转向自建插件与子代理体系、多端共享一个本地后台服务。MIT 协议。</td>
</tr>
<tr>
<td width="170"><b>NovelAI</b><br><a href="https://novelai.net/">官网</a></td>
<td width="130" align="center"><img src="原画/thumbs/novelai.jpg" width="120"></td>
<td>NovelAI 由 Anlatan 运营，是订阅制 AI 创作平台，本体是「写作加绘画」双产品。文本侧是自研微调模型序列，配 <b>Lorebook</b>（把角色、地点、世界规则结构化，模型按需召回以维持长篇一致性）。绘画侧是自行定制的 <b>Stable Diffusion</b> 衍生模型，在 <b>Danbooru 数据集</b>上训练，专攻二次元风格，支持图生图、局部重绘与画布编辑。</td>
</tr>
<tr>
<td width="170"><b>ZCode（智谱）</b><br><a href="https://zcode-ai.com/">官网</a> · <a href="https://zcode-ai.com/cn/docs">文档</a></td>
<td width="130" align="center"><img src="原画/thumbs/zcode.jpg" width="120"></td>
<td>ZCode 是智谱（Zhipu AI）出品的 <b>AI 编程工作台（Agentic Development Environment）</b>，自研 Agent 内核，深度适配自家旗舰模型。桌面、浏览器、终端共用一套工作区，同一任务内持续保持目标、文件、终端结果与 Git 状态，从规划推进到实现与验证。支持 <b>MCP</b> 与执行模式权限管理，并可通过微信、飞书、Telegram 的 Bot 通道远程下发指令与查看进度。以 Apache-2.0 协议开源。</td>
</tr>
</table>

---

## 文档导航

| 文档 | 内容 |
| --- | --- |
| [docs/角色设定与设计规律.md](docs/角色设定与设计规律.md) | 22 个对象的层级归类、技术本体速查表、设计符号与真实技术特性的对应关系 |
| [docs/官方链接索引.md](docs/官方链接索引.md) | 22 个对象的官网 / 文档 / 代码仓库入口，按用途分类跳转 |
| [docs/来源与版权.md](docs/来源与版权.md) | 逐图来源表（作品页 / 原图路径 / 尺寸）、来源链路图、三类主体区分、版权与使用提示 |
| [docs/素材来源导航.md](docs/素材来源导航.md) | 跨模型统一形象、DeepSeek娘专题、通用素材与框架、厂商官方吉祥物，共 40+ 链接 |

## 快速索引

| 类型 | 内容 |
| --- | --- |
| **本仓库收录** | 22 张白底全身立绘（22 个对象），同一画师创作，分辨率 1152×2048 / 2160×3840 / 3072×5504 |
| **同系列但非立绘** | 另有换装版、四季封面、设定表、梗图等 7 件作品，与本仓库统一风格不符、且作者归属更混杂（Ninon / Muto66），**未随本仓库发布**；其逐图来源与授权状态仍在 [docs/来源与版权.md](docs/来源与版权.md) 中完整可查 |
| **创作者** | ZipZipPipe（B 站 UID 4168597）绘制本系列全部立绘 |
| **归档方** | lmy414（蓝色大肥鱼站点 + 原图仓 + 设定图集）、ObeyYourHeart（FUMO 图鉴）——**仅获收录与下载许可** |

## 目录结构

```
AI娘原画/
├── README.md                 本文件
├── LICENSE                   双轨许可：文字 CC BY 4.0 / 图片保留所有权利
├── 原画/                     22 张完整立绘原画
│   └── thumbs/               表格内嵌缩略图（宽 ≤220px）
└── docs/                     详细文档
```

---

## 授权与使用

本仓库为**非官方**的技术索引与素材溯源项目，与任何被收录的厂商、平台、作者或站点均无隶属、背书或合作关系。仓库采用**双轨许可**（完整条款见 [LICENSE](LICENSE)）：

| 对象 | 授权 |
| --- | --- |
| README、docs/ 下全部文字内容 | **CC BY 4.0** —— 可自由使用、改编、再发布，需署名、标注许可、注明改动 |
| `原画/` 下 22 张立绘及缩略图 | **保留所有权利** —— 著作权归 ZipZipPipe（B 站 UID 4168597）所有。本仓库仅获收录与下载许可，原作品页授权字段标记为 `license-unknown`（未授予任何明确开放许可）。**禁止商业使用、二次分发、转售、去除署名，或打包重新分发** |

需要二次使用图片时，请回到原作品页联系原作者取得授权。

---

*最后更新：2026-10-25。溯源方式：抓取蓝色大肥鱼站 24 个角色页 + 全部 54 页作品列表 + 526 个作品详情页 → 解析 JSON-LD（创作者 / 版权声明 / 授权 / 尺寸 / 描述）→ 下载原图并逐张做完整性校验与白底特征检测 → 本目录图片与站点预览缩略图做整图灰度相关度匹配，22/22 命中相关度 1.000（完全一致）。全程未做任何截图、裁切或切片。*

> **关于技术描述的时效性**：本表刻意只写**架构机制、能力方向、协议授权**这类相对稳定的结构性事实，**不写具体版本号、跑分、价格、份额与发布日期** —— 这些数字更新极快，写进仓库文档必然过期。每行末尾的官方链接是查证最新信息的入口，请以官方文档为准。
