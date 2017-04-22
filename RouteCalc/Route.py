# timedelta, datetime, and date classes
from datetime import timedelta, datetime, date, time

start_num = 1
cur_num = 1
end_of_day = time(17, 0, 0)
steps = {}


# Return the step object at the current index
def get_cur_step():
    return steps[cur_num]


# Return the step object at a specific place in the list of steps
def get_step(step_num):
    return steps[step_num]


# Return the next two steps
def get_next_two():
    return get_step(cur_num + 1), get_step(cur_num + 2)


# Set the start step num at the start of a new day
def set_day_start():
    global start_num, cur_num
    start_num = cur_num


# Return the amount of time between two times
def get_time_between(begin_time, end_time):
    return end_time - begin_time


# Return the ideal time to get through the step, based on speed limit
def get_ideal_time(step_num):
    return timedelta(seconds=steps[step_num].interval /
                             steps[step_num - 1].speed) * 3600


# Return the actual time the car took to complete the step
def get_actual_time(step_num):
    return datetime.combine(date.today(), steps[step_num].time_completed) \
           - datetime.combine(date.today(), steps[step_num - 1].time_completed)


# Add a step to the list of steps, giving the step object and step number
def add_step(step_obj, step_num):
    steps[step_num] = step_obj


# Set the current step to the given step number
def set_cur_step(step_num):
    global cur_num
    cur_num = step_num


# Advance the current step by one
def advance_step():
    global cur_num
    set_time_completed(cur_num, datetime.now().time())
    cur_num += 1


# Get the distance between two steps
def get_dist_between(begin_step_num, end_step_num):
    return steps[end_step_num].distance - steps[begin_step_num].distance


# Get the speed in km/h needed to go the given distance in the given time
def get_speed(total_dist, t_time):
    return total_dist / t_time.total_seconds() * 3600


# Save the time in the desired step as the time completed
def set_time_completed(step_num, time_completed):
    steps[step_num].time_completed = time_completed


# Return the step that the car is predicted to be at by the given time
def get_predicted_step(cur_time=datetime.now().time(), end_time=end_of_day):
    global start_num, cur_num
    weighted_ratio = 0
    time_left = datetime.combine(date.today(), end_time) - \
                datetime.combine(date.today(), cur_time)
    adv_num = cur_num

    for ndx in range(start_num + 1, cur_num):
        weighted_ratio += get_actual_time(ndx).total_seconds() \
                          / get_ideal_time(ndx).total_seconds() * \
                          steps[ndx].interval

    weighted_ratio /= get_dist_between(start_num, cur_num - 1)

    time_left -= timedelta(seconds=get_ideal_time(adv_num)
                           .total_seconds() * weighted_ratio)

    while time_left > timedelta(seconds=0):
        adv_num += 1
        time_left -= timedelta(seconds=get_ideal_time(adv_num)
                               .total_seconds() * weighted_ratio)

    return steps[adv_num - 1]
