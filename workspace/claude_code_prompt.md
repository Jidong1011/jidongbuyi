# AI五层封装元能力系统 - Claude Code开发提示词

## 项目背景
基于一堂AI训站营的五层封装模型（提示词→Skill→Agent→Openclaw→AI组织），需要构建一个可运行的AI健康顾问系统原型。

## 你的任务
作为AI系统架构师，帮我实现一个**Layer 1-3**的MVP版本：
1. 提示词元能力系统（角色定义、上下文管理、输出格式化）
2. Skill封装层（饮食分析、建议生成、周报生成3个核心Skill）
3. Agent基础框架（感知-决策-行动循环）

## 技术栈要求
- **语言**: Python 3.11+
- **LLM接口**: 支持OpenAI/Claude API（使用统一抽象层）
- **配置管理**: Pydantic + YAML
- **日志**: structlog
- **测试**: pytest
- **类型提示**: 全类型注解

## 项目结构
```
ai_health_advisor/
├── pyproject.toml              # 项目配置
├── README.md                   # 使用文档
├── config/
│   ├── prompts/               # 第一层：提示词模板
│   │   ├── role_definer.yaml
│   │   ├── context_manager.yaml
│   │   └── output_formatter.yaml
│   ├── skills/                # 第二层：Skill配置
│   │   ├── meal_analyzer.yaml
│   │   ├── advice_generator.yaml
│   │   └── weekly_report.yaml
│   └── agent.yaml             # 第三层：Agent配置
├── src/
│   ├── __init__.py
│   ├── core/                  # 核心元能力
│   │   ├── __init__.py
│   │   ├── prompting.py       # L1: 提示词元能力
│   │   ├── skill.py          # L2: Skill元能力
│   │   └── agent.py          # L3: Agent元能力
│   ├── skills/               # 具体Skill实现
│   │   ├── __init__.py
│   │   ├── base.py           # Skill基类
│   │   ├── meal_analyzer.py  # 饮食分析Skill
│   │   ├── advice_generator.py # 建议生成Skill
│   │   └── weekly_report.py  # 周报生成Skill
│   ├── agent/                # Agent实现
│   │   ├── __init__.py
│   │   ├── perception.py     # 感知器
│   │   ├── decision.py       # 决策引擎
│   │   ├── action.py         # 行动执行器
│   │   └── state.py          # 状态管理
│   ├── models/               # 数据模型
│   │   ├── __init__.py
│   │   ├── user.py           # 用户模型
│   │   ├── meal.py           # 饮食记录
│   │   └── analysis.py       # 分析结果
│   └── utils/                # 工具函数
│       ├── __init__.py
│       ├── llm_client.py     # LLM客户端封装
│       └── logger.py         # 日志配置
├── tests/                    # 测试
│   ├── __init__.py
│   ├── test_prompting.py
│   ├── test_skills.py
│   └── test_agent.py
└── examples/                 # 示例
    ├── demo_meal_analysis.py
    └── demo_daily_workflow.py
```

## 详细需求

### L1: 提示词元能力 (src/core/prompting.py)

#### 1. RoleDefiner 角色定义器
```python
class RoleDefiner:
    """定义AI角色身份、专长、语气"""
    
    def __init__(self, role_config: RoleConfig):
        self.identity = role_config.identity
        self.expertise = role_config.expertise
        self.tone = role_config.tone
        
    def generate_system_prompt(self) -> str:
        """生成系统提示词"""
        return f"""你是{self.identity}。

专业领域：{', '.join(self.expertise)}

沟通风格：{self.tone}

核心职责：
1. 分析用户的饮食照片和记录
2. 提供个性化的营养建议
3. 追踪用户的健康目标进度

约束条件：
- 必须基于用户提供的信息，不能编造
- 必须添加医疗免责声明
- 保持亲切专业的语气"""
```

#### 2. ContextManager 上下文管理器
```python
class ContextManager:
    """管理对话上下文和历史记忆"""
    
    def __init__(self, max_history: int = 20):
        self.max_history = max_history
        self.history: List[Message] = []
        
    def add_message(self, role: str, content: str):
        """添加消息到历史"""
        self.history.append(Message(role=role, content=content))
        if len(self.history) > self.max_history:
            self._compress_history()
    
    def _compress_history(self):
        """压缩历史：保留关键节点，摘要化早期对话"""
        # 实现摘要逻辑
        pass
        
    def get_context_window(self, window_size: int = 10) -> str:
        """获取最近的上下文窗口"""
        recent = self.history[-window_size:]
        return self._format_messages(recent)
```

#### 3. OutputFormatter 输出格式化器
```python
class OutputFormatter:
    """规范输出结构"""
    
    def __init__(self, template_name: str):
        self.template = self._load_template(template_name)
    
    def format_daily_analysis(self, data: MealAnalysis) -> str:
        """格式化每日分析输出"""
        return f"""## 📊 今日饮食分析

**总热量**: {data.calories} kcal
**碳水化合物**: {data.carbs}g
**蛋白质**: {data.protein}g
**脂肪**: {data.fat}g

### 💡 建议
{data.suggestions}

### ⚠️ 注意
{data.warnings}

---
*免责声明：以上建议仅供参考，不构成医疗诊断*"""
```

### L2: Skill元能力 (src/core/skill.py 和 src/skills/)

#### Skill基类
```python
from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Any, Dict

class SkillInput(BaseModel):
    """Skill输入基类"""
    pass

class SkillOutput(BaseModel):
    """Skill输出基类"""
    success: bool
    error_message: str = ""

class BaseSkill(ABC):
    """Skill基类"""
    
    name: str
    description: str
    input_schema: type[SkillInput]
    output_schema: type[SkillOutput]
    
    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client
        self.logger = get_logger(self.name)
    
    @abstractmethod
    async def execute(self, input_data: SkillInput) -> SkillOutput:
        """执行Skill的核心逻辑"""
        pass
    
    async def run(self, **kwargs) -> SkillOutput:
        """带错误处理的运行入口"""
        try:
            input_data = self.input_schema(**kwargs)
            self.logger.info(f"Executing {self.name}", input=input_data)
            result = await self.execute(input_data)
            self.logger.info(f"Completed {self.name}", output=result)
            return result
        except Exception as e:
            self.logger.error(f"Failed {self.name}", error=str(e))
            return self.output_schema(success=False, error_message=str(e))
```

#### 具体Skill实现

**Skill 1: MealAnalyzer 饮食分析Skill**
```python
class MealAnalyzerInput(SkillInput):
    food_description: str  # 食物描述（文本或图像识别结果）
    user_profile: UserProfile  # 用户档案

class MealAnalyzerOutput(SkillOutput):
    nutrition: NutritionData  # 营养成分
    analysis: str  # 分析结论
    suggestions: List[str]  # 具体建议

class MealAnalyzer(BaseSkill):
    """分析饮食内容，提取营养信息"""
    
    name = "meal_analyzer"
    description = "分析用户的饮食记录，提取营养成分和健康建议"
    input_schema = MealAnalyzerInput
    output_schema = MealAnalyzerOutput
    
    async def execute(self, input_data: MealAnalyzerInput) -> MealAnalyzerOutput:
        # 1. 构建分析提示词
        prompt = self._build_analysis_prompt(input_data)
        
        # 2. 调用LLM分析
        response = await self.llm.generate(
            prompt=prompt,
            temperature=0.3,  # 低温度保证准确性
            response_format={"type": "json_object"}
        )
        
        # 3. 解析并验证结果
        analysis_data = json.loads(response)
        nutrition = NutritionData(**analysis_data["nutrition"])
        
        return MealAnalyzerOutput(
            success=True,
            nutrition=nutrition,
            analysis=analysis_data["analysis"],
            suggestions=analysis_data["suggestions"]
        )
```

**Skill 2: AdviceGenerator 建议生成Skill**
```python
class AdviceGeneratorInput(SkillInput):
    meal_analysis: MealAnalyzerOutput  # 饮食分析结果
    user_goal: UserGoal  # 用户目标（减重/控糖/增肌）
    history: List[PastAdvice]  # 历史建议（避免重复）

class AdviceGeneratorOutput(SkillOutput):
    daily_advice: str  # 每日建议
    action_items: List[str]  # 行动项
    encouragement: str  # 鼓励话语

class AdviceGenerator(BaseSkill):
    """基于分析结果生成个性化建议"""
    
    name = "advice_generator"
    description = "基于饮食分析生成个性化健康建议"
    input_schema = AdviceGeneratorInput
    output_schema = AdviceGeneratorOutput
    
    async def execute(self, input_data: AdviceGeneratorInput) -> AdviceGeneratorOutput:
        # 实现建议生成逻辑
        pass
```

**Skill 3: WeeklyReportGenerator 周报生成Skill**
```python
class WeeklyReportInput(SkillInput):
    daily_records: List[DailyRecord]  # 7天记录
    user_goal: UserGoal

class WeeklyReportOutput(SkillOutput):
    summary: str  # 本周总结
    trends: TrendsData  # 趋势数据
    next_week_plan: str  # 下周计划

class WeeklyReportGenerator(BaseSkill):
    """汇总一周数据生成周报"""
    
    name = "weekly_report_generator"
    description = "生成周度健康报告"
    input_schema = WeeklyReportInput
    output_schema = WeeklyReportOutput
```

### L3: Agent元能力 (src/core/agent.py 和 src/agent/)

#### Agent核心框架
```python
class HealthAdvisorAgent:
    """白芸豆健康顾问Agent"""
    
    def __init__(
        self,
        role_definer: RoleDefiner,
        context_manager: ContextManager,
        output_formatter: OutputFormatter,
        skills: Dict[str, BaseSkill],
        config: AgentConfig
    ):
        self.role = role_definer
        self.context = context_manager
        self.formatter = output_formatter
        self.skills = skills
        self.config = config
        self.state = AgentState.IDLE
        
    # ============== 感知层 ==============
    async def perceive(self, user_input: UserInput) -> Perception:
        """感知用户输入"""
        perception = Perception(
            input_type=self._classify_input(user_input),
            content=user_input.content,
            intent=self._extract_intent(user_input),
            urgency=self._assess_urgency(user_input)
        )
        return perception
    
    def _classify_input(self, input_data: UserInput) -> InputType:
        """分类输入类型：饮食记录/问题咨询/打卡"""
        if "吃了" in input_data.content or "照片" in input_data.content:
            return InputType.MEAL_RECORD
        elif "建议" in input_data.content:
            return InputType.ADVICE_REQUEST
        return InputType.GENERAL_CHAT
    
    # ============== 决策层 ==============
    async def decide(self, perception: Perception) -> Decision:
        """决策下一步行动"""
        rules = [
            DecisionRule(
                condition=lambda p: p.input_type == InputType.MEAL_RECORD,
                action="analyze_meal",
                skill=self.skills["meal_analyzer"]
            ),
            DecisionRule(
                condition=lambda p: p.input_type == InputType.ADVICE_REQUEST,
                action="generate_advice",
                skill=self.skills["advice_generator"]
            ),
        ]
        
        for rule in rules:
            if rule.condition(perception):
                return Decision(action=rule.action, skill=rule.skill)
        
        return Decision(action="chat", skill=None)
    
    # ============== 行动层 ==============
    async def act(self, decision: Decision, perception: Perception) -> ActionResult:
        """执行决策"""
        if decision.skill:
            result = await decision.skill.run(
                food_description=perception.content,
                user_profile=self.config.user_profile
            )
            return ActionResult(success=result.success, data=result)
        else:
            # 直接聊天回复
            response = await self._chat_response(perception)
            return ActionResult(success=True, data=response)
    
    # ============== 主循环 ==============
    async def run(self, user_input: UserInput) -> str:
        """Agent主运行循环"""
        # 1. 感知
        perception = await self.perceive(user_input)
        
        # 2. 决策
        decision = await self.decide(perception)
        
        # 3. 行动
        result = await self.act(decision, perception)
        
        # 4. 格式化输出
        if result.success:
            formatted = self.formatter.format_daily_analysis(result.data)
            return formatted
        else:
            return "抱歉，处理您的请求时出现了问题，请重试。"
```

## 配置文件示例

### config/prompts/role_definer.yaml
```yaml
role: "白芸豆AI健康顾问"
identity: "你的专属营养健康助手"
expertise:
  - 营养学
  - 白芸豆控卡原理
  - 体重管理
  - 健康饮食规划
tone: "亲切专业，像朋友一样鼓励你"
constraints:
  - "必须基于用户提供的信息，不能编造"
  - "必须添加医疗免责声明"
  - "保持积极正向的鼓励语气"
```

### config/skills/meal_analyzer.yaml
```yaml
skill_name: "meal_analyzer"
description: "分析饮食内容，提取营养信息"
input_schema:
  food_description: "string"
  user_profile: "UserProfile"
output_schema:
  nutrition:
    calories: "number"
    carbs: "number"
    protein: "number"
    fat: "number"
  analysis: "string"
  suggestions: "list[string]"
prompt_template: |
  你是一位专业的营养师，请分析以下饮食内容：
  
  食物描述：{food_description}
  
  用户档案：{user_profile}
  
  请提供：
  1. 估算的营养成分（热量、碳水、蛋白质、脂肪）
  2. 简要分析这顿饭的健康程度
  3. 给出3条具体的改进建议
  
  请以JSON格式返回。
```

## 测试要求

为每个模块编写测试：

```python
# tests/test_prompting.py
def test_role_definer():
    config = RoleConfig(
        identity="测试营养师",
        expertise=["营养学"],
        tone="专业"
    )
    definer = RoleDefiner(config)
    prompt = definer.generate_system_prompt()
    
    assert "测试营养师" in prompt
    assert "营养学" in prompt
    assert "免责声明" in prompt

# tests/test_skills.py
@pytest.mark.asyncio
async def test_meal_analyzer():
    skill = MealAnalyzer(mock_llm_client)
    result = await skill.run(
        food_description="午餐：麻辣烫，有青菜、豆腐、粉丝",
        user_profile=UserProfile(goal="减重", weight=70)
    )
    
    assert result.success
    assert result.nutrition.calories > 0
    assert len(result.suggestions) >= 3
```

## 验收标准

1. ✅ 可运行的Python代码，通过`pytest`测试
2. ✅ 包含3个核心Skill（饮食分析、建议生成、周报）
3. ✅ Agent能完成"感知→决策→行动"完整循环
4. ✅ 包含配置文件和示例脚本
5. ✅ 代码有完整类型注解和文档字符串
6. ✅ README包含安装和运行说明

## 额外加分项（可选）

- [ ] 添加CLI交互界面
- [ ] 实现简单的记忆存储（JSON文件）
- [ ] 添加LangSmith集成用于调试
- [ ] 实现Skill链式调用（Chain）

---

现在开始实现，先创建项目结构和基础框架，然后逐个实现三个Skill，最后整合Agent主循环。