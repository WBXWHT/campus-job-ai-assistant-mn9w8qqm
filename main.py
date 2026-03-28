import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class CampusJobAIAssistant:
    """校园智能求职助手核心类"""
    
    def __init__(self):
        # 模拟用户数据存储
        self.user_profiles = {}
        # 模拟岗位数据库
        self.job_database = self._init_job_database()
        # 模拟用户行为日志
        self.user_behavior_logs = []
        
    def _init_job_database(self) -> List[Dict]:
        """初始化模拟岗位数据库"""
        return [
            {"id": 1, "title": "AI产品经理实习生", "company": "科技公司A", 
             "skills": ["产品设计", "用户调研", "数据分析", "AI知识"], "match_score": 0},
            {"id": 2, "title": "软件开发工程师", "company": "科技公司B",
             "skills": ["Python", "Java", "系统设计"], "match_score": 0},
            {"id": 3, "title": "数据分析师", "company": "互联网公司C",
             "skills": ["SQL", "Python", "统计学", "数据可视化"], "match_score": 0}
        ]
    
    def register_user(self, student_id: str, major: str, skills: List[str]) -> Dict:
        """用户注册功能"""
        profile = {
            "student_id": student_id,
            "major": major,
            "skills": skills,
            "registration_date": datetime.now().strftime("%Y-%m-%d"),
            "last_active": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.user_profiles[student_id] = profile
        self._log_behavior(student_id, "user_registration", "用户注册成功")
        return profile
    
    def optimize_resume(self, student_id: str, original_resume: str) -> Dict:
        """模拟AI简历优化功能（实际项目中会调用GPT API）"""
        if student_id not in self.user_profiles:
            return {"error": "用户未注册"}
        
        # 模拟AI优化过程
        optimized_sections = [
            "优化了工作经历描述，突出量化成果",
            "根据岗位要求调整了技能展示顺序",
            "增强了项目经历的技术细节描述",
            "优化了自我评价部分，更符合AI行业特点"
        ]
        
        # 模拟AI生成的优化建议
        ai_suggestions = [
            "建议增加1-2个与AI相关的项目经历",
            "技术栈描述可以更具体，如列出使用的框架和工具",
            "量化描述工作成果，如'提升效率25%'"
        ]
        
        result = {
            "original_length": len(original_resume),
            "optimized_sections": optimized_sections,
            "ai_suggestions": ai_suggestions,
            "optimization_score": random.randint(70, 95),  # 模拟优化评分
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self._log_behavior(student_id, "resume_optimization", f"简历优化完成，评分：{result['optimization_score']}")
        return result
    
    def mock_interview(self, student_id: str, job_title: str) -> Dict:
        """模拟AI面试功能"""
        if student_id not in self.user_profiles:
            return {"error": "用户未注册"}
        
        # 模拟AI面试问题库
        interview_questions = {
            "AI产品经理实习生": [
                "请描述你理解的AI产品经理与传统产品经理的区别",
                "如何评估一个AI功能的价值？",
                "如果用户对AI生成的简历优化建议不满意，你会如何处理？"
            ],
            "软件开发工程师": [
                "请解释面向对象编程的三个主要特性",
                "描述一次你解决复杂技术问题的经历",
                "如何保证代码的质量和可维护性？"
            ]
        }
        
        questions = interview_questions.get(job_title, ["请介绍一下你自己", "为什么对这个岗位感兴趣？"])
        
        # 模拟AI反馈
        feedback = {
            "strengths": [
                "对AI产品有较好的理解",
                "回答结构清晰",
                "能够结合实际案例"
            ],
            "improvements": [
                "可以更深入地讨论技术实现细节",
                "建议准备更多数据支持的案例",
                "可以加强业务场景的思考"
            ],
            "overall_score": random.randint(60, 95)
        }
        
        result = {
            "job_title": job_title,
            "questions": questions,
            "feedback": feedback,
            "interview_duration": f"{random.randint(15, 45)}分钟",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self._log_behavior(student_id, "mock_interview", f"模拟面试完成，岗位：{job_title}")
        return result
    
    def job_matching(self, student_id: str) -> List[Dict]:
        """岗位匹配度分析功能"""
        if student_id not in self.user_profiles:
            return []
        
        user_skills = self.user_profiles[student_id]["skills"]
        
        # 计算匹配度
        matched_jobs = []
        for job in self.job_database:
            # 简单匹配算法：计算技能重叠度
            required_skills = job["skills"]
            matched_skills = [skill for skill in user_skills if skill in required_skills]
            match_score = int((len(matched_skills) / len(required_skills)) * 100) if required_skills else 0
            
            job_copy = job.copy()
            job_copy["match_score"] = min(match_score, 95)  # 设置上限
            job_copy["matched_skills"] = matched_skills
            job_copy["missing_skills"] = [skill for skill in required_skills if skill not in user_skills]
            
            # 高匹配度提醒（模拟核心功能）
            if match_score >= 70:
                job_copy["high_match_alert"] = True
                job_copy["alert_message"] = "高匹配度岗位！建议立即投递"
            else:
                job_copy["high_match_alert"] = False
                job_copy["alert_message"] = ""
            
            matched_jobs.append(job_copy)
        
        # 按匹配度排序
        matched_jobs.sort(key=lambda x: x["match_score"], reverse=True)
        
        self._log_behavior(student_id, "job_matching", f"岗位匹配完成，最高匹配度：{matched_jobs[0]['match_score'] if matched_jobs else 0}%")
        return matched_jobs
    
    def get_user_activity(self, days: int = 7) -> Dict:
        """获取用户活跃度统计（模拟周活跃度分析）"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # 统计活跃用户
        active_users = set()
        for log in self.user_behavior_logs:
            log_time = datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S")
            if start_date <= log_time <= end_date:
                active_users.add(log["student_id"])
        
        # 模拟活跃度提升（如描述中的25%提升）
        base_activity = max(1, len(active_users) - 3)  # 模拟基线
        activity_increase = 0.25  # 25%提升
        
        return {
            "period": f"最近{days}天",
            "active_user_count": len(active_users),
            "total_actions": len(self.user_behavior_logs),
            "core_feature_usage": {
                "resume_optimization": sum(1 for log in self.user_behavior_logs if log["action"] == "resume_optimization"),
                "mock_interview": sum(1 for log in self.user_behavior_logs if log["action"] == "mock_interview"),
                "job_matching": sum(1 for log in self.user_behavior_logs if log["action"] == "job_matching")
            },
            "activity_increase_percentage": activity_increase * 100,
            "simulated_impact": f"核心功能周活跃度提升{activity_increase * 100}%"
        }
    
    def _log_behavior(self, student_id: str, action: str, details: str):
        """记录用户行为日志"""
        log_entry = {
            "student_id": student_id,
            "action": action,
            "details": details,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.user_behavior_logs.append(log_entry)
        
        # 更新用户最后活跃时间
        if student_id in self.user_profiles:
            self.user_profiles[student_id]["last_active"] = log_entry["timestamp"]

def main():
    """主函数：演示校园智能求职助手核心功能"""
    print("=" * 50)
    print("校园智能求职助手 AI Agent 演示")
    print("=" * 50)
    
    # 初始化助手
    assistant = CampusJobAIAssistant()
    
    # 模拟用户注册
    print("\n1. 用户注册")
    student_profile = assistant.register_user(
        student_id="2023001",
        major="计算机科学",
        skills=["Python", "产品设计", "用户调研", "数据分析", "AI知识"]
    )
    print(f"注册成功：{json.dumps(student_profile, indent=2, ensure_ascii=False)}")
    
    # 简历优化功能
    print("\n2. AI简历优化")
    resume_result = assistant.optimize_resume(
        student_id="2023001",
        original_resume="计算机专业学生，有产品实习经历，熟悉Python和数据分析..."
    )
    print(f"优化结果：")
    print(f"  优化评分：{resume_result['optimization_score']}分")
    print(f"  AI建议：{resume_result['ai_suggestions'][0]}")
    
    # 模拟面试功能
    print("\n3. AI模拟面试")
    interview_result = assistant.mock_interview(
        student_id="2023001",
        job_title="AI产品经理实习生"
    )
    print(f"面试岗位：{interview_result['job_title']}")
    print(f"面试问题示例：{interview_result['questions'][0]}")
    print(f"AI反馈评分：{interview_result['feedback']['overall_score']}分")
    
    # 岗位匹配功能
    print("\n4. 智能岗位匹配")
    matched_jobs = assistant.job_matching(student_id="2023001")
    print("匹配结果：")
    for job in matched_jobs[:2]:  # 显示前2个结果
        alert_msg = f" ({job['alert_message']})" if job['high_match_alert'] else ""
        print(f"  {job['title']} @ {job['company']}: {job['match_score']}%匹配{alert_msg}")
    
    # 活跃度分析
    print("\n5. 用户活跃度分析")
    activity_report = assistant.get_user_activity(days=7)
    print(f"统计周期：{activity_report['period']}")
    print(f"活跃用户数：{activity_report['active_user_count']}")
    print(f"核心功能使用情况：")
    for feature, count in activity_report['core_feature_usage'].items():
        feature_cn = {"resume_optimization": "简历优化", "mock_interview": "模拟面试", "job_matching": "岗位匹配"}[feature]
        print(f"  {feature_cn}: {count}次")
    print(f"模拟效果：{activity_report['simulated_impact']}")
    
    print("\n" + "=" * 50)
    print("演示结束。实际项目中会集成真实GPT API和数据库")
    print("=" * 50)

if __name__ == "__main__":
    main()