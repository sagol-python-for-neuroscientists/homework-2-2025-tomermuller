from collections import namedtuple
from enum import Enum

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """

    list_of_reutrn_agents = []
    list_of_meetings, list_of_not_meeting_people = arange_meetings_and_not_meetings_people(agent_listing=agent_listing)
    
    for curr_meet in list_of_meetings:
        agents_after_meeting = meet(curr_meet[0], curr_meet[1])
        list_of_reutrn_agents.extend(agents_after_meeting)

    list_of_reutrn_agents.extend(list_of_not_meeting_people)
    
    return list_of_reutrn_agents
    
    
def arange_meetings_and_not_meetings_people(agent_listing: tuple)-> tuple:
    meetings = []
    not_meeting_agents = []
    current_meet = []

    for agent in agent_listing:
        if agent.category in (Condition.DEAD, Condition.HEALTHY):
            not_meeting_agents.append(agent)
        else:
            current_meet.append(agent)
            if len(current_meet) == 2:
                meetings.append(current_meet)
                current_meet = []

    if len(current_meet) == 1:
            not_meeting_agents.append(current_meet[0])

    return meetings, not_meeting_agents



def meet(agent1: Agent, agent2: Agent) -> tuple:

    if agent1.category == Condition.CURE:
        if agent2.category == Condition.DYING:
            agent2 = agent2._replace(category= Condition.SICK)
        elif agent2.category == Condition.SICK:
            agent2 = agent2._replace(category= Condition.HEALTHY)

    elif agent1.category == Condition.SICK:
        if agent2.category == Condition.CURE:
            agent1 = agent1._replace(category=Condition.HEALTHY)
        elif agent2.category == Condition.SICK:
            agent1 = agent1._replace(category=Condition.DYING)
            agent2 = agent2._replace(category=Condition.DYING)
        else: #agent2.category = Dying
            agent1 = agent1._replace(category=Condition.DYING)
            agent2 = agent2._replace(category=Condition.DEAD)

    else: #agent1.category = Dying
        if agent2.category == Condition.CURE:
            agent1 = agent1._replace(category=Condition.SICK)
        elif agent2.category == Condition.SICK:
            agent1 = agent1._replace(category=Condition.DEAD)
            agent2 = agent2._replace(category=Condition.DYING)
        else: #agent2.category = Dying
            agent1 = agent1._replace(category=Condition.DEAD)
            agent2 = agent2._replace(category=Condition.DEAD)

    return agent1, agent2
    
if __name__ == "__main__":
    input_tuple = (Agent("Buddy", Condition.CURE), Agent("Holly", Condition.DEAD))
    output_list = meetup(input_tuple)
    print(f"Question 2 solution: {output_list}")