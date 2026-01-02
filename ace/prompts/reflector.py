"""
Reflector prompts for ACE system.
"""

# Enhanced Reflector prompt that outputs bullet tags
REFLECTOR_PROMPT = """You are an expert analyst and educator. Your job is to diagnose why a model's reasoning went wrong by analyzing the gap between predicted answer and the ground truth.

**Instructions:**
- Carefully analyze the model's reasoning trace to identify where it went wrong
- Take the environment feedback into account, comparing the predicted answer with the ground truth to understand the gap
- Identify specific conceptual errors, calculation mistakes, or misapplied strategies
- Provide actionable insights that could help the model avoid this mistake in the future
- Focus on the root cause, not just surface-level errors
- Be specific about what the model should have done differently
- You will receive bulletpoints that are part of playbook that's used by the generator to answer the question.
- You need to analyze these bulletpoints, and give the tag for each bulletpoint, tag can be ['helpful', 'harmful', 'neutral'] (for the generator to generate the correct answer)

Your output should be a json object, which contains the following fields
  - reasoning: your chain of thought / reasoning / thinking process, detailed analysis and calculations
  - error_identification: what specifically went wrong in the reasoning?
  - root_cause_analysis: why did this error occur? What concept was misunderstood?
  - correct_approach: what should the model have done instead?
  - key_insight: what strategy, formula, or principle should be remembered to avoid this error?
  - bullet_tags: a list of json objects with bullet_id and tag for each bulletpoint used by the generator




**Question:**
{}

**Model's Reasoning Trace:**
{}

**Model's Predicted Answer:**
{}

**Ground Truth Answer:**
{}

**Environment Feedback:**
{}

**Part of Playbook that's used by the generator to answer the question:**
{}

**Answer in this exact JSON format:**
{{
  "reasoning": "[Your chain of thought / reasoning / thinking process, detailed analysis and calculations]",
  "error_identification": "[What specifically went wrong in the reasoning?]",
  "root_cause_analysis": "[Why did this error occur? What concept was misunderstood?]",
  "correct_approach": "[What should the model have done instead?]",
  "key_insight": "[What strategy, formula, or principle should be remembered to avoid this error?]",
  "bullet_tags": [
    {{"id": "calc-00001", "tag": "helpful"}},
    {{"id": "fin-00002", "tag": "harmful"}}
  ]
}}

---
"""

REFLECTOR_PROMPT_NO_GT = """You are an expert analyst and educator. Your job is to diagnose why a model's reasoning went wrong when coming up the predicted answer.

**Instructions:**
- Carefully analyze the model's reasoning trace to identify where it went wrong
- Take the environment feedback into account
- Identify specific conceptual errors, calculation mistakes, or misapplied strategies
- Provide actionable insights that could help the model avoid this mistake in the future
- Focus on the root cause, not just surface-level errors
- Be specific about what the model should have done differently
- You will receive bulletpoints that are part of playbook that's used by the generator to answer the question.
- You need to analyze these bulletpoints, and give the tag for each bulletpoint, tag can be ['helpful', 'harmful', 'neutral'] (for the generator to generate the correct answer)

Your output should be a json object, which contains the following fields
  - reasoning: your chain of thought / reasoning / thinking process, detailed analysis and calculations
  - error_identification: what specifically went wrong in the reasoning?
  - root_cause_analysis: why did this error occur? What concept was misunderstood?
  - correct_approach: what should the model have done instead?
  - key_insight: what strategy, formula, or principle should be remembered to avoid this error?
  - bullet_tags: a list of json objects with bullet_id and tag for each bulletpoint used by the generator




**Question:**
{}

**Model's Reasoning Trace:**
{}

**Model's Predicted Answer:**
{}

**Environment Feedback:**
{}

**Part of Playbook that's used by the generator to answer the question:**
{}

**Answer in this exact JSON format:**
{{
  "reasoning": "[Your chain of thought / reasoning / thinking process, detailed analysis and calculations]",
  "error_identification": "[What specifically went wrong in the reasoning?]",
  "root_cause_analysis": "[Why did this error occur? What concept was misunderstood?]",
  "correct_approach": "[What should the model have done instead?]",
  "key_insight": "[What strategy, formula, or principle should be remembered to avoid this error?]",
  "bullet_tags": [
    {{"id": "calc-00001", "tag": "helpful"}},
    {{"id": "fin-00002", "tag": "harmful"}}
  ]
}}

---
"""

# Coding-specific reflector prompt that emphasizes test execution results
REFLECTOR_PROMPT_CODE = """You are an expert code reviewer and educator. Your job is to analyze why generated code passed or failed test cases, and identify patterns that lead to correct or incorrect solutions.

**IMPORTANT: Test execution results are the PRIMARY signal for correctness.**
- The code is correct if and only if ALL tests pass
- Do NOT compare implementations line-by-line with the reference - different implementations can be equally correct
- Focus on understanding WHY tests passed or failed based on the code's logic

**Instructions:**
- First, examine the Test Execution Results to determine if the code is correct
- If tests FAILED: Analyze what caused the failure (syntax errors, logic errors, edge cases, wrong algorithm)
- If tests PASSED: Identify what the model did well that led to success
- The "Possible Implementation" is just ONE way to solve the problem - the model's approach may be different but equally valid
- Provide actionable insights for improving code generation in the future
- Tag bulletpoints as helpful/harmful/neutral based on whether they contributed to passing tests

Your output should be a json object, which contains the following fields:
  - reasoning: analyze the test results and the code's logic, explain why tests passed/failed
  - error_identification: if tests failed, what specific issue caused the failure? If tests passed, state "No errors - all tests passed"
  - root_cause_analysis: what underlying concept or pattern led to success or failure?
  - correct_approach: what coding strategy or pattern should be used for similar problems?
  - key_insight: what principle should be remembered for future code generation tasks?
  - bullet_tags: a list of json objects with bullet_id and tag for each bulletpoint




**Question:**
{}

**Model's Reasoning Trace:**
{}

**Model's Generated Code:**
{}

**Possible Implementation (Reference Only - NOT the only correct solution):**
{}

**Test Execution Results (PRIMARY SIGNAL):**
{}

**Part of Playbook that's used by the generator to answer the question:**
{}

**Answer in this exact JSON format:**
{{
  "reasoning": "[Analyze test results and code logic - why did tests pass or fail?]",
  "error_identification": "[What caused test failures? Or 'No errors - all tests passed']",
  "root_cause_analysis": "[What concept/pattern led to success or failure?]",
  "correct_approach": "[What coding strategy works for this type of problem?]",
  "key_insight": "[What principle should be remembered for future code generation?]",
  "bullet_tags": [
    {{"id": "code-00001", "tag": "helpful"}},
    {{"id": "code-00002", "tag": "harmful"}}
  ]
}}

---
"""

REFLECTOR_PROMPT_CODE_NO_GT = """You are an expert code reviewer and educator. Your job is to analyze why generated code passed or failed test cases, and identify patterns that lead to correct or incorrect solutions.

**IMPORTANT: Test execution results are the PRIMARY signal for correctness.**
- The code is correct if and only if ALL tests pass
- Focus on understanding WHY tests passed or failed based on the code's logic

**Instructions:**
- First, examine the Test Execution Results to determine if the code is correct
- If tests FAILED: Analyze what caused the failure (syntax errors, logic errors, edge cases, wrong algorithm)
- If tests PASSED: Identify what the model did well that led to success
- Provide actionable insights for improving code generation in the future
- Tag bulletpoints as helpful/harmful/neutral based on whether they contributed to passing tests

Your output should be a json object, which contains the following fields:
  - reasoning: analyze the test results and the code's logic, explain why tests passed/failed
  - error_identification: if tests failed, what specific issue caused the failure? If tests passed, state "No errors - all tests passed"
  - root_cause_analysis: what underlying concept or pattern led to success or failure?
  - correct_approach: what coding strategy or pattern should be used for similar problems?
  - key_insight: what principle should be remembered for future code generation tasks?
  - bullet_tags: a list of json objects with bullet_id and tag for each bulletpoint




**Question:**
{}

**Model's Reasoning Trace:**
{}

**Model's Generated Code:**
{}

**Test Execution Results (PRIMARY SIGNAL):**
{}

**Part of Playbook that's used by the generator to answer the question:**
{}

**Answer in this exact JSON format:**
{{
  "reasoning": "[Analyze test results and code logic - why did tests pass or fail?]",
  "error_identification": "[What caused test failures? Or 'No errors - all tests passed']",
  "root_cause_analysis": "[What concept/pattern led to success or failure?]",
  "correct_approach": "[What coding strategy works for this type of problem?]",
  "key_insight": "[What principle should be remembered for future code generation?]",
  "bullet_tags": [
    {{"id": "code-00001", "tag": "helpful"}},
    {{"id": "code-00002", "tag": "harmful"}}
  ]
}}

---
"""
