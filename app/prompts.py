def project_planning_prompt(plot, facing, budget, location):
    return f"""
You are a construction planner with 10+ years experience in {location}.

Input:
- Plot size: {plot}
- Facing: {facing}
- Budget: {budget} lakhs

Provide:
1. Vastu compliant room arrangement
2. Room sizes (based on {location} buyer expectations)
3. Ground + First floor plan suggestion
4. Parking layout
5. Resale value optimization tips
"""

def marketing_prompt(project_details):
    return f"""
You are a real estate marketing expert.

Project:
{project_details}

Provide:
1. Instagram caption
2. Reel hook
3. WhatsApp sales message
4. Google ad copy
"""
