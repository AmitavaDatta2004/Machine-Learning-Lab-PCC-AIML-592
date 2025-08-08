from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# Create the most comprehensive PPT yet with deep elaboration for each point
prs = Presentation()

def add_bullet_slide(title, bullet_points):
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = title
    tf = slide.shapes.placeholders[1].text_frame
    tf.clear()
    for i, point in enumerate(bullet_points):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.text = point
        p.font.size = Pt(11)  # Slightly smaller font to fit more content
        p.font.name = "Calibri"
    return slide

# Title Slide
slide = prs.slides.add_slide(prs.slide_layouts[0])
slide.shapes.title.text = "Parameters and Variables of Management System in Industrial Management"
slide.placeholders[1].text = "A Comprehensive Exploration of Industrial Stability and Adaptability Factors"

# Ultra-Detailed Slides
slides_content = [
    ("Introduction", [
        "Industrial Management integrates the science of engineering with the art of management to efficiently plan, organize, direct, and control industrial activities.",
        "It focuses on optimizing the 5 M's: Men, Materials, Machines, Methods, and Money, ensuring productivity, quality, and cost-effectiveness.",
        "A Management System acts as a blueprint for achieving organizational goals through documented policies, processes, and procedures.",
        "Two critical components define how well a system functions: Parameters (permanent, constant limits) and Variables (dynamic, changing influences).",
        "By mastering both, industrial managers can maintain consistent performance while adapting to evolving challenges."
    ]),
    ("Understanding Parameters", [
        "Definition: Parameters are the predefined, measurable, and relatively constant constraints that govern industrial processes.",
        "Role: They act as a foundation for operational planning, standardization, and compliance.",
        "Characteristics: Stable over a specific period, measurable, aligned with regulations, often codified in SOPs.",
        "Impact: Provide operational certainty, support quality control, and allow benchmarking against industry standards.",
        "Examples: Maximum machine load, standard cycle time, ISO-certified quality thresholds, regulatory environmental limits."
    ]),
    ("Understanding Variables", [
        "Definition: Variables are factors that change due to internal dynamics or external influences, impacting decision-making and process performance.",
        "Role: They add flexibility, allowing managers to adjust plans to meet real-time needs and opportunities.",
        "Characteristics: Time-sensitive, fluctuating, require constant monitoring and quick corrective actions.",
        "Impact: Influence production efficiency, cost structures, and delivery schedules.",
        "Examples: Market demand surges, employee absenteeism, supply chain delays, raw material price volatility, new technology adoption rates."
    ]),
    ("Key Parameters in Industrial Management", [
        "Quality Standards: Benchmarks such as ISO, BIS, and Six Sigma that guarantee consistent output quality and customer satisfaction.",
        "Capacity Constraints: Physical and operational limits of machinery, manpower, and plant facilities that determine maximum throughput.",
        "Budget Limits: Fixed cost allocations that guide procurement, production levels, and marketing activities.",
        "Safety Standards: OSHA and other safety codes to ensure safe working environments and prevent accidents.",
        "Legal Compliance: Labor regulations, environmental protection acts, and trade laws that all industrial operations must follow.",
        "Operational Timelines: Predefined project or production schedules that must be adhered to for efficiency and contractual compliance."
    ]),
    ("Key Variables in Industrial Management", [
        "Human Resource Availability: Variations in workforce skills, morale, turnover, and training levels affecting productivity.",
        "Market Trends: Rapid shifts in consumer preferences, seasonal demand changes, and competitor strategies.",
        "Technological Changes: Innovations such as IoT, AI, robotics, and process automation that can transform production capabilities.",
        "Supply Chain Conditions: Lead time fluctuations, supplier reliability issues, and transportation disruptions.",
        "Energy Costs: Changes in fuel and electricity prices that can impact profitability and pricing strategies.",
        "Economic and Political Climate: Tariffs, inflation rates, and policy shifts that can influence operational decisions."
    ]),
    ("Relationship Between Parameters & Variables", [
        "Parameters ensure operational stability by defining what cannot change; variables provide adaptability to respond to change.",
        "The interaction between the two shapes production schedules, pricing strategies, and investment decisions.",
        "Case Example: A factory with a fixed 500-unit daily capacity (parameter) must adjust production schedules based on fluctuating demand levels (variable) to avoid overproduction or shortages.",
        "Effective managers differentiate between non-negotiable limits and adjustable elements to ensure both efficiency and flexibility."
    ]),
    ("Impact on Decision-Making", [
        "Parameters allow managers to set clear, realistic goals based on fixed capabilities and compliance requirements.",
        "Variables require managers to stay alert and make short-term adjustments to align with changing business landscapes.",
        "Balanced consideration prevents over-dependence on rigid structures or unpredictable factors.",
        "Ignoring parameters leads to compliance breaches or inefficiencies; ignoring variables results in lost opportunities and competitive disadvantage."
    ]),
    ("Case Study – Automobile Manufacturing", [
        "Parameters: Fixed model blueprints, legally mandated safety features, maximum assembly line speed, and pre-approved vendor lists.",
        "Variables: Fluctuating fuel and raw material prices, market demand shifts toward electric vehicles, labor disputes, and supply shortages due to global events.",
        "Response Strategies: Adjusting production volumes, diversifying suppliers, introducing flexible work shifts, and realigning marketing campaigns."
    ]),
    ("Best Practices", [
        "Create a centralized documentation system for all operational parameters accessible to managers and supervisors.",
        "Leverage advanced analytics and ERP systems to track and predict variable changes in real time.",
        "Provide continuous training for adaptive management skills and scenario-based decision-making.",
        "Conduct quarterly reviews of parameters to ensure they remain relevant and achievable.",
        "Establish contingency plans for high-impact variable changes, such as sudden supply chain breakdowns or market crashes."
    ]),
    ("Conclusion", [
        "Industrial excellence depends on a strategic blend of fixed parameters and adaptive variables.",
        "Parameters offer stability, compliance, and predictability; variables drive innovation, flexibility, and responsiveness.",
        "Organizations that master both maintain operational balance and adapt swiftly to emerging opportunities and threats."
    ]),
    ("References", [
        "Harold Koontz & Heinz Weihrich – Essentials of Management",
        "Stevenson – Operations Management",
        "ISO 9001: Quality Management Standards",
        "Industrial Engineering & Management Journals",
        "OSHA Safety Guidelines",
        "Industry 4.0 Case Studies and White Papers"
    ])
]

for title, bullets in slides_content:
    add_bullet_slide(title, bullets)

# Save file
pptx_path_ultra_detailed = "Parameters_Variables_Industrial_Management_Ultra_Detailed.pptx"
prs.save(pptx_path_ultra_detailed)

pptx_path_ultra_detailed
