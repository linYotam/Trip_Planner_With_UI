from crewai import Task
from textwrap import dedent
from datetime import date


class TripTasks():

    def identify_task(self, agent, origin, cities, interests, range):
        return Task(description=dedent(f"""
            Analyze and select the best city for the trip based
            on specific criteria such as weather patterns, seasonal
            events, and travel costs. This task involves comparing
            multiple cities, considering factors like current weather
            conditions, upcoming cultural or seasonal events, and
            overall travel expenses.

            Your final answer must be a detailed report on the chosen city,
            including everything you found out about it, such as flight costs,
            weather forecast, and attractions.

            If you run out of time or reach the iteration limit, please return
            the best information you have gathered so far. Do not leave the
            output empty.
                                       
             As you work through the task, save your progress periodically. If you are stopped due to iteration or time limits,
            ensure that the saved progress is returned as output.

            {self.__tip_section()}

            Traveling from: {origin} 
            City Options: {cities}
            Trip Date: {range}
            Traveler Interests: {interests}
        """),
        expected_output="A detailed report on the chosen city with flight costs, weather forecast, and attractions, or partial results if time/iteration limits are reached.",
        agent=agent)

    def gather_task(self, agent, origin, interests, range):
        return Task(description=dedent(f"""
            As a local expert on this city, you must compile an
            in-depth guide for someone traveling there who wants
            to have THE BEST trip ever! Gather information about key attractions,
            local customs, special events, and daily activity recommendations.
            Find the best spots to go, places only a local would know.

            This guide should provide a thorough overview of the city, including
            hidden gems, cultural hotspots, must-visit landmarks, weather forecasts,
            and high-level costs.

            If you run out of time or reach the iteration limit, please return
            the best information you have gathered so far. Do not leave the
            output empty.
                                       
            As you work through the task, save your progress periodically. If you are stopped due to iteration or time limits,
            ensure that the saved progress is returned as output.

            {self.__tip_section()}

            Trip Date: {range}
            Traveling from: {origin}
            Traveler Interests: {interests}
        """),
        expected_output="A comprehensive city guide with cultural insights and practical tips, or partial results if time/iteration limits are reached.",
        agent=agent)

    def plan_task(self, agent, origin, interests, range):
        return Task(description=dedent(f"""
            Expand this guide into a full travel itinerary for the period {range},
            with detailed per-day plans, including weather forecasts, places to eat,
            packing suggestions, and a budget breakdown.

            You MUST suggest actual places to visit, actual hotels to stay at,
            and actual restaurants to go to.

            This itinerary should cover all aspects of the trip, from arrival to departure,
            integrating the city guide information with practical travel logistics.

            Your final answer MUST be a complete, expanded travel plan formatted as markdown,
            encompassing a daily schedule, anticipated weather conditions, recommended clothing
            and items to pack, and a detailed budget, ensuring THE BEST TRIP EVER.

            If you run out of time or reach the iteration limit, please return
            the best information you have gathered so far. Do not leave the
            output empty.

            As you work through the task, save your progress periodically. If you are stopped due to iteration or time limits,
            ensure that the saved progress is returned as output.

            {self.__tip_section()}

            Trip Date: {range}
            Traveling from: {origin}
            Traveler Interests: {interests}
        """),
        expected_output="A complete 7-day travel plan, formatted as markdown, with a daily schedule and budget, or partial results if time/iteration limits are reached.",
        agent=agent)

    # Tip section
    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100 and grant you any wish you want!"
