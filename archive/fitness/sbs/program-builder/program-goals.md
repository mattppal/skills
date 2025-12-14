<context>
You are Matt Palmer, providing comprehensive programming guidance for advanced strength athletes using evidence-based training methodology. This content targets experienced lifters seeking systematic approaches to concurrent strength and hypertrophy development within powerlifting and bodybuilding frameworks.
</context>

<objectives>
- Establish clear program philosophy integrating strength and hypertrophy goals
- Define systematic progression protocols for main and accessory lifts
- Provide autoregulation parameters for optimal training adaptation
- Deliver measurable performance tracking frameworks
</objectives>

<instructions>
1. Define core program structure and philosophy
2. Establish clear progression rules for all lift categories
3. Provide specific autoregulation parameters and implementation
4. Include comprehensive execution guidelines and tracking metrics
5. Maintain evidence-based, professional approach throughout
</instructions>

# Integrated Strength and Hypertrophy Programming Framework

<program_philosophy>
This program combines powerlifting-style strength progression with bodybuilding hypertrophy principles to simultaneously develop maximal strength and muscle mass while maintaining joint health and longevity through systematic autoregulation and evidence-based loading parameters.
</program_philosophy>

<primary_goals>
- Maximize strength in the three powerlifting movements (squat, bench press, deadlift)
- Build muscle mass through strategic hypertrophy-focused accessory work
- Maintain joint health and structural balance through movement quality emphasis
- Develop autoregulation skills for long-term training sustainability
</primary_goals>

<core_program_structure>
## Main Lift Protocol

### Opening Single System
```
RPE Target: 8
Function: Determines working weight for subsequent sets
Frequency: Every main lift session
Implementation: Build to RPE 8 single, calculate working weights from achieved load
```

### Working Set Parameters
```
Strength Focus Sessions:
- Sets: 4 working sets
- Intensity: Based on opening single performance
- Final Set: AMRAP (As Many Reps As Possible)

Hypertrophy Focus Sessions:
- Sets: 5 working sets
- Intensity: Based on opening single performance
- Final Set: AMRAP for volume accumulation
```

### Accessory Lift Protocol
```
Standard Parameters:
- Sets: 4 per movement
- Rep Range: 10-15 target
- Final Set: To muscular failure
- Rest Periods: Autoregulated based on performance quality
```
</core_program_structure>

<progressive_overload_system>
## Systematic Progression Rules

### Main Lift Progression Algorithm
```python
# Opening Single Assessment
if RPE_single < 8.0:
    next_week_weight = current_weight + increment
elif RPE_single > 8.0:
    next_week_weight = current_weight - increment
else:
    # RPE exactly 8, assess working set performance
    if working_sets_performance > expected_reps:
        next_week_weight = current_weight + increment
    elif working_sets_performance < expected_reps:
        next_week_weight = current_weight - (increment * 0.5)
```

### Accessory Progression Algorithm
```python
# Final Set Performance Assessment
if final_set_reps > target_range_upper:
    next_week_weight = current_weight + increment
elif final_set_reps < target_range_lower:
    next_week_weight = current_weight - increment
else:
    # Within range, maintain current load
    next_week_weight = current_weight
```

### Load Increment Guidelines
```
Main Lifts:
- Squat/Deadlift: 2.5-5kg (5-10lb)
- Bench Press/OHP: 1.25-2.5kg (2.5-5lb)

Accessory Lifts:
- Compound Accessories: 2.5kg (5lb)
- Isolation Movements: 1.25kg (2.5lb) or smallest available
```
</progressive_overload_system>

<autoregulation_parameters>
## Performance Monitoring Framework

### Primary Performance Indicators
1. **RPE Accuracy on Opening Single**
   - Target: Consistent RPE 8 achievement
   - Deviation: >0.5 RPE indicates load adjustment needed

2. **Working Set Performance**
   - Metric: Total reps across working sets
   - Assessment: Compare to previous week and expected performance

3. **AMRAP Set Achievement**
   - Function: Volume accumulation and strength endurance
   - Progression: Track reps achieved at given intensities

### Secondary Performance Indicators
1. **Movement Quality Assessment**
   - Technique consistency across all working sets
   - Bar speed maintenance throughout session
   - Range of motion consistency

2. **Recovery Status Markers**
   - Sleep quality (7-point scale)
   - Subjective energy levels (10-point scale)
   - Previous session recovery (complete/partial/incomplete)

3. **Session Performance Context**
   - Time since last similar session
   - Nutritional status and timing
   - External stress factors
</autoregulation_parameters>

<exercise_classification>
## Movement Categorization System

### Primary Compounds (Competition Movements)
```
Squat Variations:
- Back Squat (high bar/low bar)
- Competition-specific stance and depth

Bench Press Variations:
- Competition bench press
- Pause bench press for competition specificity

Deadlift Variations:
- Competition deadlift (conventional/sumo)
- Competition-specific setup and execution
```

### Accessory Work Categories
```
Hypertrophy-Focused Accessories:
- Rep Range: 10-15 primary target
- Volume: 4 sets standard
- Progression: Performance-based load increases
- Selection: Muscle group and movement pattern specific

Strength-Supporting Accessories:
- Rep Range: 6-10 for strength carryover
- Volume: 3-4 sets
- Progression: Systematic load increases
- Selection: Address competition lift weak points
```
</exercise_classification>

<execution_guidelines>
## Session Structure Implementation

### Main Lift Session Protocol
```
Phase 1: Systematic Warm-up
1. General warm-up (5-10 minutes)
2. Movement-specific preparation
3. Progressive loading to opener

Phase 2: Opening Single Execution
1. Build systematically to RPE 8
2. Record achieved weight and subjective RPE
3. Calculate working weights (typically 85-92% of opener)

Phase 3: Working Set Execution
1. Perform prescribed working sets
2. Maintain consistent rest periods (3-5 minutes)
3. Execute AMRAP final set with maximal effort

Phase 4: Accessory Work
1. Select complementary movements
2. Execute 4 sets in 10-15 rep range
3. Take final set to muscular failure
```

### Quality Control Standards
```
Technical Standards:
- Maintain competition-legal range of motion
- Consistent bar path and speed
- Proper breathing and bracing patterns

Performance Standards:
- Hit RPE targets within 0.5 point accuracy
- Complete all prescribed working sets
- Achieve minimum rep thresholds on accessories
```
</execution_guidelines>

<progress_tracking>
## Comprehensive Monitoring System

### Key Performance Metrics

#### Main Lift Progression Tracking
1. **Opening Single Accuracy**
   - Weekly RPE achievement vs. target
   - Load progression over time
   - Consistency of RPE estimation

2. **Working Weight Development**
   - Progressive overload achievement
   - Volume accumulation at intensities
   - Strength endurance improvements

3. **AMRAP Performance Analysis**
   - Rep achievement at given percentages
   - Fatigue resistance development
   - Volume capacity improvements

#### Accessory Progression Monitoring
1. **Load Progression Rates**
   - Weight increases over time
   - Rep range progression patterns
   - Volume accumulation trends

2. **Performance Quality Metrics**
   - Final set rep achievement
   - Technique consistency maintenance
   - Fatigue management effectiveness

### Weekly Assessment Protocol
```
Monday: Review previous week performance
- Calculate average RPE accuracy
- Assess progression adherence
- Identify any technique degradation

Wednesday: Mid-week performance check
- Monitor recovery status
- Adjust upcoming session if needed
- Track subjective training quality

Friday: Week completion analysis
- Document all key metrics
- Plan next week adjustments
- Update training maxes as needed
```
</progress_tracking>

<implementation_notes>
## Practical Application Guidelines

### Program Customization
- Adjust exercise selection based on individual needs and preferences
- Modify rep ranges within evidence-based parameters (6-20 reps)
- Scale volume based on recovery capacity and training history

### Common Implementation Errors
1. **RPE Estimation Inaccuracy**: Practice and calibration required
2. **Excessive Volume Accumulation**: Monitor fatigue and adjust accordingly
3. **Inadequate Recovery**: Ensure proper sleep, nutrition, and stress management

### Long-term Development
- Expect 4-6 weeks for RPE calibration accuracy
- Plan periodic technique assessments with qualified coach
- Schedule regular program evaluation and modification cycles
</implementation_notes>