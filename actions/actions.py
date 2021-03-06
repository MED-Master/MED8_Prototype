# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from Plots import plotting
from foldercreation import folder
from text2num import text2num

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []


class PlotTimelineOfDNT(Action):#1

    def name(self) -> Text:
        return "PlotTimelineOfDNT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the timeline for door to needle times!")
        plotting.dnt_timeline(plotting, "Dates", "DNT (Median)", plotting.df, folder.baseFolder, "Change in DNT over time", ["Lyon"], "Hospital")
        return []

class PlotlocalComparisonsTimelineOfDNT(Action): #2

    def name(self) -> Text:
        return "PlotlocalComparisonsTimelineOfDNT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the DNT timeline for other local hospitals!")
        plotting.dnt_timeline(plotting, "Dates", "DNT (Median)", plotting.df, folder.baseFolder,
                              "Mean DNT over time with local hospitals", ["France", "Lyon"], "Country")

        return []


class PlotAnnotateDNTLocalHospitals(Action): #4

    def name(self) -> Text:
        return "PlotAnnotateDNTLocalHospitals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the annotation with the DNT of local hospitals")
        plotting.annotate_timeline_event(plotting, "Dates", "DNT (Median)", plotting.df, folder.baseFolder,
                                          ["France", "Lyon"], "Country")


        return []


class PlotCompareToCountry(Action): #6

    def name(self) -> Text:
        return "PlotCompareToCountry"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your DNT times are above most other hospitals both in and out of Europe. However, you have similar times to other hospitals who have a similar high intake of patients.")
        plotting.create_international_timeline_plot("Dates", "DNT (Median)", plotting.df, folder.baseFolder,
                              "Mean DNT compared internationally",["France", "Lyon", "Slovakia", "South Africa", "Peru", "Denmark"], "Country", False)

        return []

class PlotCompareToCountry_alt(Action): #6_alt

    def name(self) -> Text:
        return "PlotCompareToCountry_alt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your DNT times are above most other hospitals both in and out of Europe. However, you have similar times to other hospitals who have a similar high intake of patients.")
        plotting.create_international_timeline_plot("Dates", "DNT (Median)", plotting.df, folder.baseFolder,
                              "Mean DNT compared internationally", ["France", "Lyon", "Slovakia", "South Africa", "Peru", "Denmark"], "Country", True)

        return []


class PlotPatientOfImpact_barplot(Action): #11

    def name(self) -> Text:
        return "PlotPatientOfImpact_barplot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="As you can see here, your hospital recieves more patients than others. This can likely explain your hospital's longer door to needle times.")
        plotting.dnt_barplot_bycountry("Hospital", "Patient Intake", plotting.df, folder.baseFolder, "Comparing mean patient intake internationally (2022 Q1)")
        return []

class PlotCompareLocalHospitals(Action): #10

    def name(self) -> Text:
        return "PlotCompareLocalHospitals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        plotting.dnt_barplot_bycountry("Hospital", "DNT (Median)", plotting.df, folder.baseFolder, "Comparing mean DNT with local hospitals (2022 Q1)")
        dispatcher.utter_message(text="Your Mean DNT is 5 minutes higher than the average of local hospitals.")


        return []


class PlotTimelineOfPatientsIn(Action):#12

    def name(self) -> Text:
        return "PlotTimelineOfPatientsIn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the timeline for Patients intake!")
        plotting.dnt_timeline(plotting, "Dates", "Patient Intake", plotting.df, folder.baseFolder, "Intake of patients over time", ["Lyon"], "Hospital")
        return []


class PlotTimelineOfInVsOut(Action):#13

    def name(self) -> Text:
        return "PlotTimelineOfInVsOut"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the timeline for Patient intake against discharge!")
        plotting.Plot_InVsOut_timeline(plotting, "Dates", "Patient Intake", "Discharge", plotting.df, folder.baseFolder,
                                       ["Lyon"], "Hospital")
        #MAKE PLOT FOR THIS
        return []

class CombineInVsOut(Action):#9

    def name(self) -> Text:
        return "CombineInVsOut"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the timeline for the difference between Patient intake and discharge!")
        plotting.dnt_timeline(plotting, "Dates", "Patient Intake Vs Discharge", plotting.df, folder.baseFolder,
                                       "Patient intake - Discharge", ["Lyon"], "Hospital")
        #MAKE PLOT FOR THIS
        return []

class CombineInVsOut_local(Action):#17

    def name(self) -> Text:
        return "CombineInVsOut_local"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the comparison with local hospitals!")
        plotting.dnt_timeline(plotting, "Dates", "Patient Intake Vs Discharge", plotting.df, folder.baseFolder,
                                       "Patient intake - Discharge compared with local hospitals", ["France", "Lyon"], "Country")
        #MAKE PLOT FOR THIS
        return []

class CombineInVsOut_international(Action):#18

    def name(self) -> Text:
        return "CombineInVsOut_international"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the comparison with international hospitals!")
        plotting.create_international_timeline_plot("Dates", "Patient Intake Vs Discharge", plotting.df, folder.baseFolder,
                                       "Patient intake - Discharge compared internationally", ["France", "Lyon", "Slovakia", "South Africa", "Peru", "Denmark"], "Country", False)
        #MAKE PLOT FOR THIS
        return []

class CompareInVsOutLocal_notcombine(Action):#14

    def name(self) -> Text:
        return "CompareInVsOutLocal_notcombine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is a comparison with local hospitals!")
        plotting.Plot_InVsOut_notcombined_local("Dates", "Patient Intake", "Discharge", plotting.df, folder.baseFolder,
                                                ["France", "Lyon"], "Country")
        #MAKE PLOT FOR THIS
        return []

class CompareInVsOutInternational_notcombine(Action):#15

    def name(self) -> Text:
        return "CompareInVsOutInternational_notcombine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is a comparison with International hospitals!")
        plotting.Plot_InVsOut_notcombined_international("Dates", "Patient Intake", "Discharge", plotting.df,
                                                        folder.baseFolder, ["France", "Lyon",
                                                                            "Slovakia", "South Africa", "Peru", "Denmark"], "Country",)


        return []

class GoalSetting(Action):#16

    def name(self) -> Text:
        return "GoalSetting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        DNT_Goal = next(tracker.get_latest_entity_values('annotationForGoalSetting'), None)

        if not DNT_Goal:
            dispatcher.utter_message(text="I need a number for your DNT goal")
            return []

        else:
            if str.isdecimal(DNT_Goal) == False:
                DNT_Goal = text2num(DNT_Goal)
                DNT_Goal = str(DNT_Goal)
            dispatcher.utter_message(text="Your DNT goal is " + DNT_Goal)
            DNT_Goal = int(DNT_Goal)

            plotting.annotate_goal(plotting, "Dates", "DNT (Median)", plotting.df, folder.baseFolder,
                                                                DNT_Goal, ["France", "Lyon"], "Country")
            dispatcher.utter_message(text="Thanks for the discussion, looking forward to the next session!")
            return []



