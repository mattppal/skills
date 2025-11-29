<context>
You are Matt Palmer, providing comprehensive setup and usage instructions for the Stronger By Science program suite. This content targets advanced lifters seeking detailed guidance for implementing evidence-based training programs using the SBS spreadsheet system, covering program selection, customization, and systematic progression protocols.
</context>

<objectives>
- Provide clear, actionable setup instructions for all SBS programs
- Enable proper program selection based on individual goals and experience
- Establish systematic customization and progression frameworks
- Ensure optimal implementation of autoregulated training principles
</objectives>

<instructions>
1. Present comprehensive overview of SBS program suite and design philosophy
2. Provide detailed setup instructions for each program category
3. Explain autoregulation principles and implementation strategies
4. Include systematic progression and monitoring guidelines
5. Maintain technical precision while ensuring accessibility for advanced users
</instructions>

# Stronger By Science Program Implementation Guide

<program_suite_overview>
## SBS Program Architecture

The Stronger By Science program collection consists of evidence-based training templates designed for systematic strength and hypertrophy development across all experience levels. Each program incorporates autoregulation principles, allowing for individualized progression based on performance feedback rather than predetermined load increases.

### Program Categories
```
Strength-Focused Programs:
- SBS Strength Program (21-week periodized)
- SBS Strength Program Last Set RIR (autoregulated volume)
- SBS Strength Program Reps to Failure (maximum effort sets)

Hypertrophy-Focused Programs:
- SBS Hypertrophy Template (21-week volume-focused)
- SBS Novice Hypertrophy (open-ended progression)

Linear Progression Programs:
- SBS Linear Progression (novice strength development)

Customizable Framework:
- SBS Program Builder (advanced customization tool)
```

### Core Design Principles
```
Block Periodization Approach:
- 21-week macrocycles divided into three 7-week mesocycles
- Progressive intensity increases with corresponding volume adjustments
- Built-in deload weeks every 7 weeks for recovery optimization

Autoregulation Integration:
- RPE-based load adjustments
- Performance-driven progression decisions
- Individual response accommodation

Full-Body Training Emphasis:
- Higher frequency training for skill development
- Enhanced volume distribution across training week
- Improved training quality through reduced per-session demands
```
</program_suite_overview>

<general_setup_framework>
## Universal Setup Principles

### Initial Configuration
<setup_protocol>
**Rounding Increment Setup (Critical First Step)**
```
Purpose: Determines minimum load progression increments
Implementation:
- Pound plates with 2.5lb minimum: Set to "5"
- Kilogram plates with 1.25kg minimum: Set to "2.5"  
- Mixed equipment or precise control: Set to "0.1"

Rationale: Matches available equipment for realistic progression
```

**Training Max Establishment**
```
Conservative Approach (Recommended):
- Use 90-95% of current 1RM for main lifts
- Allows for skill development and progression runway
- Reduces risk of early program stagnation

True Max Approach:
- Use current 1RM estimates
- Program will autoregulate to appropriate levels
- Higher initial challenge but requires accurate estimation

Estimation Guidelines:
- Recent 3-5RM performances with RPE data
- Competition results within last 6 months
- Conservative estimates preferred over optimistic projections
```
</setup_protocol>

### Exercise Selection Framework
<selection_principles>
**Main Lift Selection (Primary Focus)**
```
Standard Powerlifting Setup:
- Squat: Back squat (high bar or low bar based on preference)
- Bench: Competition-style bench press
- Deadlift: Conventional or sumo based on strength/preference
- Overhead Press: Standing barbell OHP or seated variation

Sport-Specific Modifications:
- Powerlifting: Focus on competition lifts exclusively
- Strongman: Include competition-specific variations
- General Strength: Maintain balanced movement patterns
- Bodybuilding: Emphasize muscle development over competition specificity
```

**Auxiliary Lift Integration**
```
Selection Criteria:
- Close variations of main lifts maintaining similar movement patterns
- Bilateral compound movements using barbell or similar implements
- Examples: Pause squats, close-grip bench, trap bar deadlifts

Programming Guidelines:
- 2 squat auxiliaries (different stances, tempos, or equipment)
- 2 bench auxiliaries (grip width, incline, or pause variations)
- 1 deadlift auxiliary (stance opposite to main or block/rack pulls)
- 1 OHP auxiliary (seated, push press, or implement variation)
```
</selection_principles>
</general_setup_framework>

<strength_program_implementation>
## SBS Strength Program Setup

### Program Philosophy
<strength_framework>
This 21-week program prioritizes maximal strength development through systematic intensity progression while maintaining autoregulated volume adjustments. The program culminates in 1RM testing capability while building work capacity throughout the training cycle.

**Autoregulation Mechanism**
```
RIR (Reps in Reserve) Target System:
- Each main exercise has prescribed RIR targets per set
- Actual performance compared to targets drives load adjustments
- Underperformance triggers load reductions
- Overperformance triggers load increases

Performance Thresholds:
- Minimum Sets: 4 (if achieved early, reduce training max)
- Maximum Sets: 6 (if exceeded, increase training max)
- Target completion: 4-6 sets within RIR parameters
```

**Progression Algorithm**
```python
# Weekly Load Adjustment Logic
if sets_completed < minimum_threshold:
    next_week_training_max *= 0.95  # Reduce by 5%
elif sets_completed > maximum_threshold:
    next_week_training_max *= 1.025  # Increase by 2.5%
else:
    next_week_training_max *= 1.0  # Maintain current load

# Additional factors: Sleep, stress, nutrition status
if recovery_compromised:
    apply_additional_reduction(0.025)  # Extra 2.5% reduction
```
</strength_framework>

### Block Structure Implementation
<periodization_blocks>
**Block 1: Volume Accumulation (Weeks 1-7)**
```
Intensity Range: 60-80% 1RM
Rep Ranges: 4-8 reps per set
Focus: Work capacity development and technique refinement
RIR Targets: 2-4 reps in reserve

Key Adaptations:
- Neuromuscular coordination improvements
- Work capacity enhancement
- Movement pattern reinforcement
- Confidence building with manageable loads
```

**Block 2: Intensification (Weeks 8-14)**
```
Intensity Range: 70-87.5% 1RM  
Rep Ranges: 2-6 reps per set
Focus: Strength development and power enhancement
RIR Targets: 1-3 reps in reserve

Key Adaptations:
- Maximal strength improvements
- Rate of force development enhancement
- Competition skill development
- Mental preparation for heavy loading
```

**Block 3: Realization (Weeks 15-21)**
```
Intensity Range: 80-100% 1RM
Rep Ranges: 1-4 reps per set  
Focus: Peak strength expression and testing
RIR Targets: 0-2 reps in reserve

Key Adaptations:
- Peak strength demonstration
- Competition simulation
- Technical mastery under maximal loads
- Psychological readiness for limit attempts
```
</periodization_blocks>
</strength_program_implementation>

<hypertrophy_program_implementation>
## SBS Hypertrophy Template Setup

### Program Philosophy
<hypertrophy_framework>
This 21-week program optimizes muscle growth through high-volume training with moderate intensities. The program maintains strength development while prioritizing muscle hypertrophy through strategic volume progression and exercise variety.

**Volume Optimization Strategy**
```
Intensity Parameters:
- Main lifts: 65-82.5% 1RM maximum
- Rep ranges: 5-12 reps primary focus
- Volume: Higher set numbers compared to strength programs
- Frequency: Enhanced muscle group training frequency

Progression Methodology:
- Volume increases take precedence over load increases
- Multiple progression pathways (reps, sets, load)
- Exercise rotation every 4-6 weeks for continued stimulus
- Recovery optimization through strategic deloads
```

**Muscle Group Prioritization**
```
Primary Compounds:
- Squat variations: 3-4x per week exposure
- Bench variations: 3-4x per week exposure  
- Deadlift variations: 2-3x per week exposure
- Overhead pressing: 2-3x per week exposure

Accessory Integration:
- Isolation movements: 2-3x per week per muscle group
- Unilateral work: Integrated throughout program
- Weak point targeting: Customizable based on individual needs
- Injury prevention: Built into exercise selection
```
</hypertrophy_framework>

### Volume Management System
<volume_protocols>
**Progressive Volume Increases**
```
Week 1-3: Baseline Volume Establishment
- Focus on movement quality and technique mastery
- Establish individual volume tolerance baselines
- Practice autoregulation and RPE accuracy

Week 4-6: Systematic Volume Increases  
- Add 1-2 sets per muscle group based on recovery
- Monitor performance quality as volume increases
- Adjust exercise selection based on response

Week 7: Strategic Deload
- Reduce volume by 40-50% while maintaining frequency
- Emphasize movement quality and technique refinement
- Prepare for next training block progression
```

**Volume Distribution Guidelines**
| Muscle Group | Weekly Sets | Frequency | Progression Method |
|-------------|-------------|-----------|-------------------|
| Chest | 12-18 | 3-4x | Sets then reps then load |
| Back | 14-20 | 3-4x | Sets then reps then load |
| Shoulders | 10-16 | 3-4x | Reps then sets then load |
| Arms | 8-14 | 2-3x | Reps then load |
| Legs | 14-22 | 2-3x | Sets then reps then load |
| Core | 6-10 | 2-3x | Reps then frequency |
</volume_protocols>
</hypertrophy_program_implementation>

<novice_program_guidance>
## Novice Program Implementation

### Linear Progression Setup
<novice_strength_framework>
**Program Philosophy**: Simple, systematic progression focused on consistent improvement through linear load increases while developing fundamental movement competency.

**Setup Requirements**
```
Prerequisites:
- 3-6 months basic lifting experience
- Competent in squat, bench, deadlift, overhead press
- Access to progressive loading (barbell + plates)
- Consistent training schedule availability (3-4x per week)

Initial Load Selection:
- Start with weights allowing 5 reps @RPE 7-8
- Conservative approach: Use 80-85% of estimated 5RM
- Focus on perfect technique over challenging weights
- Expect 4-6 weeks of adaptation period
```

**Progression Methodology**
```python
# Simple Linear Progression Algorithm
if all_sets_completed_successfully:
    next_session_weight += standard_increment
else:
    next_session_weight = current_weight  # Repeat until successful

# Standard Increments
squat_increment = 2.5kg  # (5lbs)
deadlift_increment = 2.5kg  # (5lbs)  
bench_increment = 1.25kg  # (2.5lbs)
overhead_press_increment = 1.25kg  # (2.5lbs)

# Deload Protocol (when progression stalls)
if failed_same_weight_3_consecutive_sessions:
    deload_weight = current_weight * 0.90
    restart_progression_from_deload_weight
```
</novice_strength_framework>

### Novice Hypertrophy Implementation
<novice_hypertrophy_framework>
**Dual Progression System**: Combines volume and intensity progression for optimal muscle growth while maintaining strength development.

**Phase 1: Volume Progression**
```
Starting Parameters: 3 sets x 8 reps @RPE 7-8
Volume Progression Sequence:
Week 1-2: 3 x 8 (establish baseline)
Week 3-4: 4 x 8 (add set)
Week 5-6: 4 x 10 (add reps)  
Week 7-8: 5 x 10 (add set)
Week 9-10: 5 x 12 (add reps)

Transition Criteria:
- Complete all prescribed sets and reps for 2 consecutive sessions
- Maintain RPE 7-8 throughout all working sets
- No technique degradation with volume increases
```

**Phase 2: Load Progression**
```
Load Increase Protocol:
- Increase weight by 2.5-5kg (5-10lbs) for lower body
- Increase weight by 1.25-2.5kg (2.5-5lbs) for upper body
- Return to 3 x 8 with new weight
- Repeat volume progression cycle

Progression Monitoring:
- Track total volume (sets x reps x weight) weekly
- Monitor RPE consistency across all working sets
- Assess recovery between sessions and weeks
- Adjust progression speed based on individual response
```
</novice_hypertrophy_framework>
</novice_program_guidance>

<program_builder_advanced>
## SBS Program Builder Customization

### Advanced Customization Framework
<builder_philosophy>
The Program Builder represents the most flexible tool in the SBS suite, allowing complete customization of training variables while maintaining evidence-based progression methodologies. This tool requires advanced understanding of training principles and individual response patterns.

**Customization Capabilities**
```
Exercise Selection:
- Unlimited exercise choices across all categories
- Mix and match progression schemes per exercise
- Custom rep ranges and intensity zones
- Periodization across multiple training blocks

Progression Schemes:
- Light Burgundy: Rep increase progression
- Gray: Set then rep increase progression  
- Teal: Classic overload progression
- Yellow: Fixed total reps progression
- Peach: Set-by-set autoregulation

Individual Optimization:
- Custom volume landmarks per muscle group
- Personalized recovery requirements
- Goal-specific exercise emphasis
- Schedule and equipment accommodations
```
</builder_philosophy>

### Implementation Strategy
<advanced_setup>
**Phase 1: Needs Analysis**
```
Individual Assessment:
- Training history and experience level
- Strength levels and weak point identification
- Recovery capacity and lifestyle factors
- Specific goals and timeline requirements
- Equipment availability and schedule constraints

Program Design Decisions:
- Training frequency (3-6 days per week)
- Session duration preferences (45-120 minutes)
- Exercise selection priorities (strength vs. hypertrophy)
- Progression methodology preferences
- Periodization timeline and structure
```

**Phase 2: Exercise Allocation**
```
Primary Movement Selection:
- Choose 3-6 main lifts based on goals
- Assign appropriate progression schemes (typically Teal or Peach)
- Establish baseline loads and rep ranges
- Plan progression timelines and testing phases

Secondary Movement Integration:
- Select 4-8 auxiliary exercises
- Balance movement patterns and muscle groups
- Assign progression schemes based on exercise type
- Coordinate with primary movement demands

Accessory Exercise Programming:
- Choose 6-12 isolation and supplementary exercises
- Focus on weak point development and injury prevention
- Utilize simpler progression schemes (Light Burgundy/Gray)
- Plan exercise rotation schedules
```

**Phase 3: Volume and Intensity Distribution**
```
Weekly Volume Planning:
- Allocate sets per muscle group based on goals
- Distribute volume across training sessions
- Balance high-intensity and moderate-intensity work
- Plan recovery and deload weeks

Progressive Overload Strategy:
- Establish progression criteria for each exercise category
- Plan load increments and timeline expectations
- Create contingency plans for plateaus and setbacks
- Monitor and adjust based on individual response
```
</advanced_setup>
</program_builder_advanced>

<autoregulation_mastery>
## RPE and Autoregulation Implementation

### RPE Scale Calibration
<rpe_framework>
**Accurate RPE estimation forms the foundation of successful autoregulated training. This skill requires practice and honest self-assessment.**

**RPE Scale Reference**
| RPE | Reps in Reserve | Description | Application |
|-----|-----------------|-------------|-------------|
| 10 | 0 | Maximum effort, no additional reps possible | Competition, testing, rare use |
| 9.5 | 0 | Could possibly do 1 more rep | Peak singles, final sets |
| 9 | 1 | Could definitely do 1 more rep | Heavy singles, strength work |
| 8.5 | 1-2 | Could do 1-2 more reps | Primary strength sets |
| 8 | 2 | Could do 2 more reps | Standard working sets |
| 7.5 | 2-3 | Could do 2-3 more reps | Volume work, accessories |
| 7 | 3 | Could do 3 more reps | Moderate intensity work |
| 6 | 4+ | Could do 4+ more reps | Warm-up, technique work |

**Calibration Protocol**
```
Week 1-2: Conservative Estimation
- Aim for RPE targets 0.5 points below prescription
- Focus on movement quality over exact RPE matching
- Record actual reps achieved vs. estimated capacity

Week 3-4: Accuracy Development
- Strive for exact RPE targets
- Practice estimating RIR before completing sets
- Compare estimates to actual performance

Week 5+: Advanced Application
- Use RPE for in-session adjustments
- Apply autoregulation principles consistently
- Develop intuitive understanding of daily readiness
```
</rpe_framework>

### Daily Autoregulation Strategies
<autoregulation_application>
**Pre-Session Assessment**
```
Readiness Indicators:
- Sleep quality and duration (7-point scale)
- Subjective energy levels (10-point scale)  
- Motivation for training (10-point scale)
- Previous session recovery status
- Life stress and external factors

Adjustment Guidelines:
- Poor sleep (<6 hours): Reduce RPE targets by 1 point
- High stress levels: Reduce volume by 20-30%
- Excellent readiness: Maintain or slightly increase intensity
- Moderate readiness: Proceed with planned training
```

**In-Session Adjustments**
```
Real-Time Modifications:
- First set performance indicates daily capacity
- Adjust subsequent sets based on initial RPE feedback
- Reduce volume if technique deteriorates significantly
- Increase load if RPE consistently below targets

Session Completion Criteria:
- Maintain movement quality standards throughout
- Achieve minimum effective volume for adaptation
- Avoid excessive fatigue that impairs recovery
- End session with positive training experience
```
</autoregulation_application>
</autoregulation_mastery>

<monitoring_and_progression>
## Performance Monitoring Framework

### Key Performance Indicators
<monitoring_system>
**Primary Metrics**
```
Strength Indicators:
- Training max progression rates across main lifts
- RPE consistency and accuracy development
- Volume progression at given intensities
- Technical proficiency maintenance under load

Hypertrophy Indicators:
- Total weekly volume accumulation
- Progressive overload across all rep ranges  
- Exercise performance improvements
- Anthropometric measurements and body composition

Recovery Indicators:
- Session completion rates and quality ratings
- Sleep quality and duration consistency
- Subjective recovery between sessions
- Motivation and training adherence patterns
```

**Tracking Protocols**
```
Daily Recording:
- All training loads, sets, and reps achieved
- RPE ratings for working sets
- Session duration and quality assessment
- Sleep and recovery data

Weekly Analysis:
- Training max adjustments and progression rates
- Volume accumulation across muscle groups
- Recovery quality and adherence patterns
- Upcoming week planning and adjustments

Monthly Evaluation:
- Performance testing and assessment
- Program satisfaction and enjoyment levels
- Goal progress and timeline adjustments
- Exercise selection review and modifications
```
</monitoring_system>

### Long-term Progression Planning
<progression_strategy>
**Periodization Integration**
```
Macrocycle Planning (12-52 weeks):
- Establish long-term strength and physique goals
- Plan competition or testing phases
- Schedule extended deload and recovery blocks
- Integrate life events and schedule changes

Mesocycle Planning (4-12 weeks):
- Focus on specific adaptations (strength, hypertrophy, power)
- Plan exercise rotations and program modifications
- Schedule regular assessment and testing phases
- Adjust volume and intensity based on adaptation

Microcycle Planning (1 week):
- Distribute volume and intensity across training days
- Plan recovery activities and lifestyle optimization
- Make real-time adjustments based on readiness
- Prepare for upcoming training challenges
```

**Continuous Improvement Process**
```
Regular Assessment Intervals:
- Weekly: Training performance and recovery analysis
- Monthly: Program effectiveness and satisfaction review
- Quarterly: Goal reassessment and program modifications  
- Annually: Comprehensive evaluation and goal setting

Adaptation Strategies:
- Identify and address weak points systematically
- Modify exercise selection based on response patterns
- Adjust volume and intensity based on recovery capacity
- Integrate new techniques and methodologies as appropriate
```
</progression_strategy>
</monitoring_and_progression>

This comprehensive guide provides the framework for implementing any SBS program effectively while developing the advanced skills necessary for long-term training success and continuous improvement.