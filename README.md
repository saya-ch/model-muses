# Model Muses · AI 拟人美术素材索引

> 一份关于「AI 模型被画成什么样」的**素材导航**，不是图片仓库

## 这个仓库是什么

社区把大模型画成角色，这件事已经持续了两年多。画的人散在 B 站、pixiv、GitHub、QQ 群，作品散在动态、合集、插件包里，没有一个地方能看全。

**这个仓库做的是把它们指出来，而不是搬过来。**

| 做什么 | 不做什么 |
| --- | --- |
| 记录**谁在画**、画了什么、在哪里能看 | 不批量转载别人的图 |
| 标注**每一张的授权**，能收的才收 | 不把「能找到」当成「可以用」 |
| 保留**来源链路**，能从一张图追到原作者 | 不做无水印合集、不做网盘打包 |

能合法收进仓库的图，都放在 [`原画/`](原画/) 下；不能收的，只在索引里留链接。

## 三份入口

| 入口 | 内容 | 规模 |
| --- | --- | --- |
| **[美术素材索引](docs/美术素材索引.md)** | **本仓库的核心**：按平台、画师、角色组织的素材地图 | 40+ 来源 |
| [主表](README.md#对照表) | 32 个对象，一对象一张白底竖版立绘，用于横向对照 | 32 张 |
| [画廊](docs/画廊.md) | 任何类型的图：立绘 / 插画 / 梗图 / 设定 / 漫画 | 59 张 |

## 对照表

**这张表的标准只有一条，而且是硬性的：白底 + 竖版 + 单人 + 全身。** 因为它的用途是对照——32 行并排看下来，谁的配色更冷、谁的识别符号更清楚，一眼能比出来。混进横版、带场景、带字的图，这个比较就失效了。

每个对象配一段技术本体说明，只写稳定事实：架构机制、能力方向、协议授权。不写版本号、跑分、价格与市场份额——这些数字更新极快，写进文档必然过期。

按层级分 12 类，因为「可对比性」其实是跨层级的：DeepSeek 和 GPT 可以比模型能力，但 DeepSeek 和 GitHub 不在同一维度。它们被放在一起，是因为社区都用拟人形象去指代它们。

> **怎么看这张表**：点左侧缩略图打开原图，点对象名进官网。想按类型随便翻翻，去 [画廊](docs/画廊.md)；想找更多素材来源，去 [美术素材索引](docs/美术素材索引.md)。

<table>
<tr>
<td width="170"><b>DeepSeek</b><br><a href="https://www.deepseek.com/">官网</a> · <a href="https://api-docs.deepseek.com/">API 文档</a> · <a href="https://github.com/deepseek-ai">GitHub</a></td>
<td width="130" align="center"><a href="原画/deepseek-ref.jpg" title="点开看原图"><img src="原画/thumbs/deepseek.jpg" width="120"></a></td>
<td>DeepSeek（深度求索）背后是量化投资公司幻方量化，模型走稀疏 MoE 路线。注意力侧从早期的 <b>MLA</b> 换到<b>混合注意力</b>——压缩稀疏注意力沿序列维度压 KV cache，叠一层深度压缩注意力兼顾密集读；结构上用<b>流形约束超连接</b>把残差映射约束到双随机矩阵流形，配 <b>Muon</b> 优化器稳收敛。训练保留<b>多 token 预测</b>，强化学习后训练走自研 <b>GRPO</b>；推理分非思考 / 高思考 / 极限三档，视觉侧以「<b>视觉原语</b>」把点与框坐标当推理单元。MIT 开放。</td>
</tr>
<tr>
<td width="170"><b>GPT（OpenAI）</b><br><a href="https://openai.com/">官网</a> · <a href="https://platform.openai.com/docs">开发者文档</a> · <a href="https://github.com/openai">GitHub</a></td>
<td width="130" align="center"><a href="原画/gpt-ref.jpg" title="点开看原图"><img src="原画/thumbs/gpt.jpg" width="120"></a></td>
<td>GPT 来自 OpenAI，是闭源前沿通用模型的代表。真正的护城河在<b>工具调用协议与生态集成</b>——结构化接口稳定驱动外部工具，长流程不易崩格式，第三方 Agent 框架的适配面最大；近年重心进一步转向<b>可执行的编程代理</b>形态，把推理直接落成对仓库与环境的操作。闭源，不可自部署。</td>
</tr>
<tr>
<td width="170"><b>Claude（Anthropic）</b><br><a href="https://www.anthropic.com/">官网</a> · <a href="https://docs.claude.com/">文档</a> · <a href="https://github.com/anthropics">GitHub</a></td>
<td width="130" align="center"><a href="原画/claude-ref.jpg" title="点开看原图"><img src="原画/thumbs/claude.jpg" width="120"></a></td>
<td>Claude 出自 Anthropic，主打<b>长程智能体可靠性与代码能力</b>。四个关键机制：<b>可调推理强度</b>（effort 从低到最高多档，另设供长程任务用的扩展档，同一模型即可切换快慢与花费）、<b>自适应思考</b>（由模型自行判断哪一步值得深想）、<b>上下文压缩</b>（接近阈值时服务端自动摘要旧上下文，可配阈值）、以及<b>提示缓存</b>（复用历史前缀，Agent 循环不重复付费）。Agent 侧已从单代理走向<b>多代理协作</b>。</td>
</tr>
<tr>
<td width="170"><b>Gemini（Google）</b><br><a href="https://deepmind.google/models/gemini/">模型页</a> · <a href="https://ai.google.dev/gemini-api/docs">API 文档</a> · <a href="https://github.com/google-deepmind">GitHub</a></td>
<td width="130" align="center"><a href="原画/gemini-ref.jpg" title="点开看原图"><img src="原画/thumbs/gemini.jpg" width="120"></a></td>
<td>Gemini 出自 Google DeepMind，是唯一以<b>原生多模态</b>为核心的全栈模型：单模型同时处理文本、图像、音频、视频、PDF 与代码，无需外挂专用模型拼接。推理深度可按档位调节；与 Google 搜索、地图等第一方服务<b>原生打通</b>，可直接注入已验证的检索结果。</td>
</tr>
<tr>
<td width="170"><b>Grok（xAI）</b><br><a href="https://x.ai/">官网</a> · <a href="https://docs.x.ai/">API 文档</a> · <a href="https://github.com/xai-org">GitHub</a></td>
<td width="130" align="center"><a href="原画/grok-ref.jpg" title="点开看原图"><img src="原画/thumbs/grok.jpg" width="120"></a></td>
<td>Grok 来自马斯克的 xAI，是通用对话与推理模型。差异点是<b>实时性</b>——检索层直接接 X 平台的数据流，DeepSearch 一类能力会读取当下社交帖子与突发新闻，而非依赖训练截止的静态知识。输出侧由 <b>Skills</b> 机制承接：把一次教会的工作流存成账号级技能，跨会话复用，并直接产出可下载的 Office 文档与 PDF；单次请求支持上百个并行工具调用。代价是来源缺少权威性筛选。</td>
</tr>
<tr>
<td width="170"><b>Kimi（月之暗面）</b><br><a href="https://www.moonshot.cn/">官网</a> · <a href="https://platform.moonshot.cn/">开放平台</a> · <a href="https://github.com/MoonshotAI">GitHub</a></td>
<td width="130" align="center"><a href="原画/kimi-ref.jpg" title="点开看原图"><img src="原画/thumbs/kimi.jpg" width="120"></a></td>
<td>Kimi 来自月之暗面（Moonshot AI），走 MoE 路线，自研 <b>Kimi Delta Attention</b> 混合线性注意力与<b>注意力残差</b>，配合量化感知训练直接产出低比特权重，支撑起百万级上下文。模型系列本身即 <b>agentic</b>，接上工具能自主完成多步任务。推理侧为<b>混合思考模式</b>。开放权重，采用带附加条件的开放许可。</td>
</tr>
<tr>
<td width="170"><b>Qwen（通义千问）</b><br><a href="https://qwenlm.github.io/">官网</a> · <a href="https://github.com/QwenLM">GitHub</a></td>
<td width="130" align="center"><a href="原画/qwen-ref.jpg" title="点开看原图"><img src="原画/thumbs/qwen.jpg" width="120"></a></td>
<td>Qwen（通义千问）是阿里云通义团队的开源模型系列，<b>覆盖最全的一条产品线</b>：轻量稠密到大规模 MoE，端侧到企业级。技术亮点是<b>混合思考模式</b>（开关切换分步推理与快速响应，配思考预算控成本）、多语言支持、统一多模态编码与<b>原生 MCP</b>。全系 Apache 2.0，商用无限制。</td>
</tr>
<tr>
<td width="170"><b>GLM（智谱）</b><br><a href="https://docs.bigmodel.cn/">开放文档</a> · <a href="https://github.com/THUDM">GitHub</a></td>
<td width="130" align="center"><a href="原画/glm-ref.jpg" title="点开看原图"><img src="原画/thumbs/glm.jpg" width="120"></a></td>
<td>GLM 出自智谱（Zhipu AI，源自清华知识工程实验室），采用 MoE 架构。<b>参数效率</b>是核心卖点——轻量版本可比肩更大的闭源模型。<b>混合推理模式</b>可切，针对工具调用、网页浏览与软件工程做了专门优化；另有<b>原生多模态分支</b>，与 OCR、语音、图像生成等细分模型构成全模态矩阵。权重以 MIT 协议开放。</td>
</tr>
<tr>
<td width="170"><b>混元（腾讯）</b><br><a href="https://github.com/Tencent-Hunyuan">GitHub</a> · <a href="https://hunyuan.tencent.com/">混元官网</a></td>
<td width="130" align="center"><a href="原画/hunyuan-ref.jpg" title="点开看原图"><img src="原画/thumbs/hunyuan.jpg" width="120"></a></td>
<td>混元是腾讯自研的大模型系列，走<b>中文语料加全模态</b>路线，文本、图像、语音、视频与 3D 生成并行推进。深度依托腾讯云与微信生态，针对中文语境与本土知识优化。开源版本覆盖语言、<b>视频世界模型</b>与 <b>3D 重建</b>方向：前者按片段生成、过程中可用文字介入改写场景，后者能在单张消费级显卡上秒级重建 3D 世界。多个项目以 Apache 2.0 协议发布。</td>
</tr>
<tr>
<td width="170"><b>豆包 Seed（字节跳动）</b><br><a href="https://seed.bytedance.com/">Seed 官网</a> · <a href="https://www.volcengine.com/docs/ark">火山方舟文档</a> · <a href="https://github.com/volcengine">GitHub</a></td>
<td width="130" align="center"><a href="原画/seed-ref.jpg" title="点开看原图"><img src="原画/thumbs/seed.jpg" width="120"></a></td>
<td>豆包 Seed 是字节跳动 Seed 团队的模型系列，经火山引擎对外提供服务，主线是<b>统一多模态架构</b>——单主干同时接收文本、图像、视频、音频并做跨模态联合推理，而非拼接多个专用模型。工程重点在视觉编码器瘦身与长上下文访存成本。产品侧另有一条<b>按周迭代的动态模型</b>，以统一模型 ID 持续推送最新版本；生成侧另有图像、视频、语音与 3D 资产的独立模型线。</td>
</tr>
<tr>
<td width="170"><b>文心一言（百度）</b><br><a href="https://yiyan.baidu.com/">产品页</a> · <a href="https://ernie.baidu.com/">文心官方博客</a> · <a href="https://github.com/PaddlePaddle/ERNIE">开源仓库</a></td>
<td width="130" align="center"><a href="原画/wenxin-ref.jpg" title="点开看原图"><img src="原画/thumbs/wenxin.jpg" width="120"></a></td>
<td>文心一言（百度，2025 年 11 月起品牌统一为「文心」）的本体是文心大模型 ERNIE 系列。技术基因是<b>知识增强</b>——预训练阶段融入大规模知识图谱。旗舰走<b>原生全模态</b>：文本、图像、音频、视频映射进同一符号空间，用统一的「<b>下一组 token 预测</b>」端到端优化，分模态再各设专门目标（视觉走下一帧与尺度预测、音频走下一编解码预测），而非在后挂专用解码器；MoE 用<b>模态无关路由</b>，专家按 token 特征而非模态分配。开源侧另有 Apache 2.0 的多模态异构 MoE 系列。</td>
</tr>
<tr>
<td width="170"><b>阶跃星辰（StepFun）</b><br><a href="https://www.stepfun.com/">官网</a> · <a href="https://platform.stepfun.com/">开放平台</a> · <a href="https://github.com/stepfun-ai">GitHub</a></td>
<td width="130" align="center"><a href="原画/stepfun-ref.jpg" title="点开看原图"><img src="原画/thumbs/stepfun.jpg" width="120"></a></td>
<td>阶跃星辰（StepFun）是 2023 年 4 月成立于上海的基础模型公司，创始人姜大昕此前任微软全球副总裁。路线是<b>原生多模态</b>——模型从训练之初就统一处理文本、图像与视频，而不是在语言主干上外挂视觉编码器。产品结构为一个 Step 基座向上生长，多模态与<b>端云结合</b>两条线并行：轻量模型下沉到手机、汽车与 IoT，另配 <b>Step-GUI</b> 一类图形界面智能体做跨应用操作，复杂任务再上云。开源与闭源 API 双轨。</td>
</tr>
<tr>
<td width="170"><b>MiMo（小米）</b><br><a href="https://mimo.xiaomi.com/zh/">官网</a> · <a href="https://www.xiaomi-mimo-ai.com/">模型站</a> · <a href="https://github.com/XiaomiMiMo">GitHub</a></td>
<td width="130" align="center"><a href="原画/mimo-ref.jpg" title="点开看原图"><img src="原画/thumbs/mimo.jpg" width="120"></a></td>
<td>MiMo 是小米自研的大模型系列，走<b>推理优先</b>路线。架构上是 MoE 加<b>动态激活</b>——按 token 选专家，把激活参数压到远小于总量，配<b>混合注意力</b>与<b>多层多 token 预测</b>，解码速度明显快于同档稠密模型。<b>端侧优先</b>是它最鲜明的取向：INT4 量化、结构化剪枝与硬件感知 kernel 让它能跑在手机、车机与音箱上，而不只是云端。产品线从端侧小模型一路铺到万亿级 MoE 旗舰，另有全模态、语音、视觉与终端编码 agent 等分支。权重以 MIT 协议开放，可商用与微调。</td>
</tr>
<tr>
<td width="170"><b>Llama（Meta）</b><br><a href="https://llama.meta.com/">官网</a> · <a href="https://huggingface.co/meta-llama">模型页</a></td>
<td width="130" align="center"><a href="原画/llama-ref.jpg" title="点开看原图"><img src="原画/thumbs/llama.jpg" width="120"></a></td>
<td>Llama 来自 Meta，是<b>开放权重路线</b>的代表：权重公开，衍生出大量微调版与量化版，主导私有化部署与学术复现生态，最新一代采用<b>早期融合的原生多模态 MoE</b> 设计。它同时是别人的底座——多个主流产品以其为基座后训练。授权为社区许可：可商用，但须标注「Built with Llama」、衍生模型名以 Llama 开头，且超出月活阈值的大平台需单独取得授权。</td>
</tr>
<tr>
<td width="170"><b>Mistral AI</b><br><a href="https://mistral.ai/">官网</a> · <a href="https://docs.mistral.ai/">文档</a> · <a href="https://github.com/mistralai">GitHub</a></td>
<td width="130" align="center"><a href="原画/mistral-ref.jpg" title="点开看原图"><img src="原画/thumbs/mistral.jpg" width="120"></a></td>
<td>Mistral AI 是一家总部位于巴黎的欧洲厂商，以<b>高效小模型与开放权重</b>著称：参数压得比同档更狠而质量不降，小尺寸系列广泛用于端侧与边缘部署，另有稀疏 MoE 版与长文档结构化输出模型。授权分层明确——多数开源模型用 Apache 2.0，部分走改版 MIT（月营收超阈值需转商业授权），旗舰模型则提供非商用免费与商业授权两条路。另有 OCR、语音等周边模型。</td>
</tr>
<tr>
<td width="170"><b>MiniMax</b><br><a href="https://www.minimax.io/">官网</a> · <a href="https://platform.minimax.io/docs">平台文档</a> · <a href="https://github.com/MiniMax-AI">GitHub</a></td>
<td width="130" align="center"><a href="原画/minimax-ref.jpg" title="点开看原图"><img src="原画/thumbs/minimax.jpg" width="120"></a></td>
<td>MiniMax（稀宇科技）是上海的基础模型公司，本体是<b>全模态自研底座</b>：文本、语音、视频、音乐全部自研而非集成他人。工程路线上以自研<b>线性注意力</b>打破注意力复杂度带来的上下文长度限制，后续转向稀疏注意力架构。生成侧已做到单模型同时输出带原生立体声的高分辨率视频——对白、音效与环境声在同一次生成中完成，靠自研的高压缩 tokenizer 降低生成开销，并开放了权重供本地部署。</td>
</tr>
<tr>
<td width="170"><b>Perplexity</b><br><a href="https://www.perplexity.ai/">官网</a> · <a href="https://docs.perplexity.ai/">API 文档</a> · <a href="https://github.com/perplexityai">GitHub</a></td>
<td width="130" align="center"><a href="原画/perplexity-ref.jpg" title="点开看原图"><img src="原画/thumbs/perplexity.jpg" width="120"></a></td>
<td>Perplexity 出自 Perplexity AI，本质是<b>检索增强生成（RAG）引擎</b>，而非参数化知识模型——每次回答都必须经过实时检索。核心资产是自建的实时网页索引，由预索引与实时抓取两套爬虫持续更新，索引层跑在 Vespa 之上；检索层混合自建索引与外部搜索 API，经相关性与权威性等多道关卡筛选后综合成带内联引用的回答。综合层使用自研 Sonar 系列（基于 Llama 后训练），并路由多家前沿闭源模型处理更难的查询；之上是能多步检索并交叉核验的深度研究模式。</td>
</tr>
<tr>
<td width="170"><b>JEV（TypeSafe AI）</b><br><a href="https://typesafe.ai/">官网</a> · <a href="https://baike.baidu.com/item/Jev/69087529">百科条目</a></td>
<td width="130" align="center"><a href="原画/jev-ref.jpg" title="点开看原图"><img src="原画/thumbs/jev.jpg" width="120"></a></td>
<td>Jev 出自 TypeSafe AI（创始人 Diogo Almeida 此前在 OpenAI 参与 ChatGPT 相关方法研究），是对「模型该输出什么」的重写：不生成文本，只把非结构化状态映射成<b>带校准概率的类型化决策</b>，直接交给程序分支。名字取自<b>杰文斯悖论</b>，定位是卡尼曼意义上的「系统一」——快判断而非慢推理。实现上是新架构加<b>并行采样器</b>：一次调用并行算完多个问题，合法答案类型调用前就声明好，故不会输出 schema 外的值（判断仍可能错）。训练用自研 <b>RLCD</b>，优化概率与真实频率的吻合度。闭源 API。</td>
</tr>
<tr>
<td width="170"><b>GitHub</b><br><a href="https://github.com/">官网</a> · <a href="https://docs.github.com/en/copilot">Copilot 文档</a></td>
<td width="130" align="center"><a href="原画/github-ref.jpg" title="点开看原图"><img src="原画/thumbs/github.jpg" width="120"></a></td>
<td>GitHub 是微软旗下的代码托管平台，<b>本体是协作基础设施而非 AI 模型</b>。对 AI 时代的影响在两条线：<b>Copilot</b> 已从编辑器补全扩展成终端里的完整 agentic 开发环境——具备计划模式与<b>自动驾驶模式</b>、内置专用子代理、并行执行与后台委派，并支持 MCP、插件、Agent Skills 与自定义 agent；此外把主流模型接入自家 Agent 与云端开发环境，直接作用于仓库、PR、Issue 与 CI。</td>
</tr>
<tr>
<td width="170"><b>GitLab</b><br><a href="https://about.gitlab.com/">官网</a> · <a href="https://docs.gitlab.com/">文档</a></td>
<td width="130" align="center"><a href="原画/gitlab-ref.jpg" title="点开看原图"><img src="原画/thumbs/gitlab.jpg" width="120"></a></td>
<td>GitLab 出自 GitLab Inc.，以 <b>DevSecOps 全生命周期</b>为定位：代码托管、CI/CD、制品管理、安全扫描、容器注册表一站式覆盖。AI 侧是 <b>GitLab Duo Agent Platform</b>——把补全、代码解释、漏洞检测与 MR 评审嵌进流水线，并作为 MCP 客户端接入外部系统；差异在于<b>把 AI 放进 DevSecOps 的每个环节</b>。有 SaaS 与自托管开源版。</td>
</tr>
<tr>
<td width="170"><b>Gitee（码云）</b><br><a href="https://gitee.com/">官网</a></td>
<td width="130" align="center"><a href="原画/gitee-ref.jpg" title="点开看原图"><img src="原画/thumbs/gitee.jpg" width="120"></a></td>
<td>Gitee（码云）由开源中国（OSCHINA）推出，是国内的代码托管平台，重心在<b>国产化适配</b>：支持信创软硬件环境、代码安全合规扫描、对接企业内部研发系统。AI 侧提供补全与对话式助手，并配套自有的模型分发平台，可对接国产大模型以满足私有化与数据不出域。</td>
</tr>
<tr>
<td width="170"><b>Cloudflare</b><br><a href="https://www.cloudflare.com/">官网</a> · <a href="https://developers.cloudflare.com/workers-ai/">Workers AI 文档</a> · <a href="https://github.com/cloudflare">GitHub</a></td>
<td width="130" align="center"><a href="原画/cloudflare-ref.jpg" title="点开看原图"><img src="原画/thumbs/cloudflare.jpg" width="120"></a></td>
<td>Cloudflare 是全球 CDN 与边缘计算平台，AI 是它网络之上的一层。本体不是模型，而是一整套边缘构建块：<b>Workers AI</b> 在全球分布的 GPU 上跑推理，按调用计费而非按预留卡时；<b>AI Gateway</b> 把 OpenAI、Anthropic 与自家推理收进同一代理入口，附缓存、限流与提示注入护栏；<b>Vectorize</b> 分布式向量库支撑 RAG，<b>D1</b> 边缘 SQLite，<b>R2</b> 零出口费；<b>Durable Objects</b> 把状态与计算合成一个原语，每个 agent 自带数据库与记忆并可休眠。差异点是<b>边缘优先</b>——推理在最近的城市完成，不必回源。</td>
</tr>
<tr>
<td width="170"><b>Hugging Face</b><br><a href="https://huggingface.co/">官网</a> · <a href="https://huggingface.co/docs/transformers/index">transformers 文档</a></td>
<td width="130" align="center"><a href="原画/huggingface-ref.jpg" title="点开看原图"><img src="原画/thumbs/huggingface.jpg" width="120"></a></td>
<td>Hugging Face 是同名公司运营的<b>模型托管与分发平台</b>，不是模型本身。核心是 Hub（模型/数据集/应用的托管与版本管理），配套的 <b>transformers</b> 库已成为开源模型加载的事实标准抽象层。该平台 2026 年 9 月与英伟达达成约 129 亿美元收购协议，官方承诺继续作为开放平台独立运营、不强制绑定自家算力。</td>
</tr>
<tr>
<td width="170"><b>LobeHub</b><br><a href="https://lobehub.com/">官网</a> · <a href="https://github.com/lobehub/lobehub">GitHub</a> · <a href="https://lobehub.com/docs">文档</a></td>
<td width="130" align="center"><a href="原画/lobehub-ref.jpg" title="点开看原图"><img src="原画/thumbs/lobehub.jpg" width="120"></a></td>
<td>LobeHub（前身 LobeChat）是开源的 <b>AI 智能体工作台</b>，本体不是模型，而是把模型接起来的那层：统一接入数十家供应商与本地 Ollama，把 <b>Agent 当作工作单元</b>——市场、群组并行协作、知识库、定时运行、分层记忆与原生 MCP；往上再设一层 <b>CAO（首席 Agent 运营官）</b>，由它拆目标、排班、派活。可自托管。许可为 <b>LobeHub 社区许可</b>：Apache 2.0 加附加条件，未修改商用允许，分发衍生作品需商业授权。</td>
</tr>
<tr>
<td width="170"><b>昇腾（华为）</b><br><a href="https://www.hiascend.com/">昇腾社区</a> · <a href="https://www.mindspore.cn/">MindSpore</a> · <a href="https://github.com/Ascend">开源仓库</a></td>
<td width="130" align="center"><a href="原画/ascend-ref.jpg" title="点开看原图"><img src="原画/thumbs/ascend.jpg" width="120"></a></td>
<td>昇腾是华为自研的 <b>AI 算力底座</b>，本体是 NPU 芯片加全栈软件，不是模型。芯片基于自研<b>达芬奇（Da Vinci）架构</b>——Cube 矩阵、Vector 向量与 Scalar 标量单元协同，同一套指令集从端侧覆盖到数据中心；新一代叠了 <b>SIMD/SIMT 双编程模型</b>与自研 <b>HBM</b>，补不规则访存与带宽短板。软件侧是 <b>CANN</b> 异构计算架构配 <b>MindSpore</b> 框架，兼容 PyTorch 与 TensorFlow。集群侧靠自研<b>灵衢</b>互联连成<b>千卡级超节点</b>，做统一内存编址与近似线性扩展。</td>
</tr>
<tr>
<td width="170"><b>RWKV</b><br><a href="https://wiki.rwkv.com/">官方 Wiki</a> · <a href="https://rwkv.cn/">中文站</a> · <a href="https://github.com/RWKV">GitHub</a></td>
<td width="130" align="center"><a href="原画/rwkv-ref.jpg" title="点开看原图"><img src="原画/thumbs/rwkv.jpg" width="120"></a></td>
<td>RWKV 由彭博（Bo Peng）提出，2023 年并入 Linux 基金会，现为其下的开源非营利项目，是一种<b>非 Transformer 架构</b>的线性注意力语言模型。原理是把 softmax 点积注意力改写为线性递推：训练时并行展开，推理时退化为 RNN——<b>显存与生成速度恒定、完全不需要 KV cache</b>。第七代架构引入动态状态演化，突破了注意力范式的表达力上限。代价是失去任意回看任意 token 的能力，长文精确回忆偏弱。权重 Apache 2.0。</td>
</tr>
<tr>
<td width="170"><b>OpenCode</b><br><a href="https://opencode.ai/">官网</a> · <a href="https://github.com/anomalyco/opencode">GitHub</a></td>
<td width="130" align="center"><a href="原画/opencode-ref.jpg" title="点开看原图"><img src="原画/thumbs/opencode.jpg" width="120"></a></td>
<td>OpenCode 由 Anomaly（原 SST）开源，本体是<b>与模型解耦的 AI 编码 agent 外壳</b>：终端、桌面、Web、IDE 扩展多形态，底层经 <b>Models.dev</b> 接入数十家供应商，也可直连各家订阅账户。工程细节上原生支持 <b>LSP</b>（用语言服务器取精确符号与诊断，而非粘贴文件内容）、多会话并行、计划与执行双模式、工具权限规则与 MCP。MIT 协议。</td>
</tr>
<tr>
<td width="170"><b>GitHub Copilot</b><br><a href="https://github.com/features/copilot">产品页</a> · <a href="https://docs.github.com/copilot">文档</a></td>
<td width="130" align="center"><a href="原画/ghcopilot-ref.jpg" title="点开看原图"><img src="原画/thumbs/ghcopilot.jpg" width="120"></a></td>
<td>GitHub Copilot 是 GitHub 的<b>编码助手产品线</b>，与平台本体分开计。形态已从编辑器补全扩成终端里的 <b>agentic 开发环境</b>：<b>计划模式</b>先摊方案让你审，<b>自动驾驶模式</b>一路做到底；内置 Explore / Task / Code Review 等子代理并行干活，加 & 前缀可把任务甩给云端 agent 后台执行。扩展面覆盖 MCP、插件与 <b>Agent Skills</b>（markdown 写的可复用工作流）。订阅制，闭源。</td>
</tr>
<tr>
<td width="170"><b>Microsoft Copilot</b><br><a href="https://www.microsoft.com/en-us/microsoft-copilot">产品页</a> · <a href="https://learn.microsoft.com/copilot/">文档</a></td>
<td width="130" align="center"><a href="原画/mscopilot-ref.jpg" title="点开看原图"><img src="原画/thumbs/mscopilot.jpg" width="120"></a></td>
<td>Microsoft Copilot 出自微软，本体是<b>模型编排层</b>而非单一模型：提问先经 <b>Prometheus / Orchestrator</b> 补检索上下文（办公走 Microsoft Graph，消费版走索引网页，代码走仓库），再按任务路由给基础模型，最后过一遍安全过滤。模型池有 OpenAI、Anthropic 与自研 <b>MAI</b> 系——Anthropic 已在商业租户默认启用；往上用 Copilot Studio 搭 agent（可接 MCP 与现成 Skills）；端侧另有 Phi 类小模型跑在带 NPU 的 PC 上。</td>
</tr>
<tr>
<td width="170"><b>NovelAI</b><br><a href="https://novelai.net/">官网</a></td>
<td width="130" align="center"><a href="原画/novelai-ref.jpg" title="点开看原图"><img src="原画/thumbs/novelai.jpg" width="120"></a></td>
<td>NovelAI 由 Anlatan 运营，是订阅制 AI 创作平台，本体是「写作加绘画」双产品。文本侧是自研微调模型序列，配 <b>Lorebook</b>（把角色、地点、世界规则结构化，模型按需召回以维持长篇一致性）。绘画侧是自行定制的 <b>Stable Diffusion</b> 衍生模型，在 <b>Danbooru 数据集</b>上训练，专攻二次元风格，支持图生图、局部重绘与画布编辑。</td>
</tr>
<tr>
<td width="170"><b>ComfyUI</b><br><a href="https://www.comfy.org/">官网</a> · <a href="https://docs.comfy.org/">文档</a> · <a href="https://github.com/Comfy-Org/ComfyUI">GitHub</a></td>
<td width="130" align="center"><a href="原画/comfyui-ref.jpg" title="点开看原图"><img src="原画/thumbs/comfyui.jpg" width="120"></a></td>
<td>ComfyUI 是开源的节点式 AI 工作流引擎，2023 年 1 月由 comfyanonymous 放上 GitHub，以 <b>GPL-3.0</b> 发布。它把生成流程拆成一张<b>有向无环图</b>：加载、编码、采样、解码各是一个节点，连线即数据流；服务端按依赖拓扑排序执行，改动哪条分支就只重跑哪条，不必整条重算。GUI、HTTP/WebSocket API 与图执行后端是三件套，同一份工作流 JSON 既能手拖也能被程序调用。它<b>不自带模型权重</b>，SD、FLUX 之类要自己放进 `models/`——工具与资产分离正是它的取向。官方只把云 GPU 与合作伙伴节点做成可选付费层，开源核心不做功能阉割。</td>
</tr>
<tr>
<td width="170"><b>ZCode（智谱）</b><br><a href="https://zcode-ai.com/">官网</a> · <a href="https://zcode-ai.com/cn/docs">文档</a></td>
<td width="130" align="center"><a href="原画/zcode-ref.jpg" title="点开看原图"><img src="原画/thumbs/zcode.jpg" width="120"></a></td>
<td>ZCode 是智谱（Zhipu AI）出品的 <b>AI 编程工作台（Agentic Development Environment）</b>，自研 Agent 内核，深度适配自家旗舰模型。桌面、浏览器、终端共用一套工作区，同一任务内持续保持目标、文件、终端结果与 Git 状态，从规划推进到实现与验证。支持 <b>MCP</b> 与执行模式权限管理，并可通过微信、飞书、Telegram 的 Bot 通道远程下发指令与查看进度。以 Apache-2.0 协议开源。</td>
</tr>
</table>

## 素材从哪来

这个仓库的图来自五类地方，每一类都有不同的授权状况：

| 类型 | 代表 | 规模 | 授权状况 |
| --- | --- | --- | --- |
| **中文归档站** | 蓝色大肥鱼站 | 1112 件 / 24 角色 | 逐图 JSON-LD，但 1040 件原作者未标注 |
| **画师本人主页** | hcz（102 件）、上善无形（294 件）、ZipZipPipe（3 件）、康壳火火火（17 件） | 416 件 | 部分有明确声明，多数需逐个确认 |
| **开源项目内置素材** | dsh-whale-galgame、TreapGoGo/deepseek-whale-girl | 170+ 件 | 有逐文件许可表，最规范 |
| **社区资源库** | AATINF 素材包（202 张）、dsh-deep-whale 皮肤（87 张） | 289 张 | 代码 MIT，但图片许可不明 |
| **百科与媒体** | 萌娘百科、媒体报道 | — | 只作线索，不作来源 |

**这一轮最大的发现是 hcz**：一位画师就有 102 件 AI 娘作品，其中 27 件 DeepSeek、10 件 ChatGPT、4 件 Claude、1 件 GLM，还做成了六个连载系列（AI Girls Comic、DeepSeek & ChatGPT、Maid DeepSeek Meme、Yuri Moment 等）。**找到一位画师，往往比翻十个站点收获更大。**

详细的来源清单、每个来源能拿到什么、以及为什么大部分没有收，见 **[美术素材索引](docs/美术素材索引.md)**。

## 授权

**没有任何一张获得商业使用许可。** 图片权利归各自作者，本仓库只做索引与有限收录。

| 对象 | 授权 |
| --- | --- |
| 全部文字（README、docs/） | **CC BY 4.0** —— 可自由使用、改编、再发布，需署名 |
| `原画/` 下图片 | 按作者声明分档：CC BY-NC-SA 4.0 / CC BY-NC / CC0 / 作者许可 / 站点未标注 |

逐图授权见 [来源与版权](docs/来源与版权.md)，完整条款见 [LICENSE](LICENSE)。

## 文档

| 文档 | 内容 |
| --- | --- |
| [docs/美术素材索引.md](docs/美术素材索引.md) | **核心**：按平台与画师组织的素材地图，含采集方法与判定标准 |
| [docs/画廊.md](docs/画廊.md) | 59 张已收图，五区分类，每张带预览与跳转 |
| [docs/画廊索引.md](docs/画廊索引.md) | 站内 1112 件作品的全量缩略图墙 |
| [docs/角色设定与设计规律.md](docs/角色设定与设计规律.md) | 32 个对象的层级归类、设计符号与技术特性的对应 |
| [docs/来源与版权.md](docs/来源与版权.md) | 逐图来源、来源链路、授权判定 |
| [docs/官方链接索引.md](docs/官方链接索引.md) | 32 个对象的官网 / 文档 / 代码仓库 |
| [data/pixiv_artists.json](data/pixiv_artists.json) | 画师作品的结构化索引（仅元数据），可直接筛选与复核 |

## 目录结构

```
AI娘原画/
├── README.md                 本文件
├── LICENSE                   双轨：文字 CC BY 4.0 / 图片按作者声明分档
├── 原画/                     32 张主表立绘（白底竖版）
│   └── thumbs/
├── 原画/画廊/                59 张画廊图，按类型分五区
│   ├── 立绘/  30 张
│   ├── 插画/  12 张
│   ├── 梗图/   8 张
│   ├── 设定/   8 张
│   └── 漫画/   1 张
├── data/                     结构化索引（仅元数据，无图片）
│   └── pixiv_artists.json    4 位画师 151 件作品的 id/标题/尺寸/标签
├── docs/                     文档
└── scripts/                  外链体检脚本
```

---

## 参与

两类贡献都不需要写代码：

| 想做什么 | 怎么做 |
| --- | --- |
| **补充素材来源** | 提 issue 给出链接、作者、授权状况即可 |
| **纠正技术描述** | 提 issue 指出哪一句过时或写错，附官方文档链接 |
| **报告失效链接** | 提 issue 说明哪个链接 404 或跳转异常 |

两条底线：**不接收图片的二次分发**（图片著作权不在维护者手上），**技术描述只写稳定事实**。

---

*最后更新：2026-10-27。溯源方式见 [来源与版权](docs/来源与版权.md)。全程未做任何截图、裁切或切片。*
