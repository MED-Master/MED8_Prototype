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

        dispatcher.utter_message(text="Here is the timeline for DNT!")
        plotting.dnt_timeline(plotting, "Dates", "DNT (Median)", plotting.df, folder.baseFolder, ["Lyon"], "Hospital")
        return []

class PlotlocalComparisonsTimelineOfDNT(Action): #2

    def name(self) -> Text:
        return "PlotlocalComparisonsTimelineOfDNT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the timeline for DNT with other local hospitals!")
        plotting.dnt_timeline(plotting, "Dates", "DNT (Median)", plotting.df, folder.baseFolder,
                              ["France", "Lyon (your hospital)"], "Country")

        return []


class PlotAnnotateDNTLocalHospitals(Action): #4

    def name(self) -> Text:
        return "PlotAnnotateDNTLocalHospitals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the annotations with the DNT of local hospitals")
        plotting.annotate_timeline_event(plotting, "Dates", "DNT (Median)", plotting.df, folder.baseFolder,
                                         ["France", "Lyon (your hospital)"], "Country")


        return []


class PlotCompareToCountry(Action): #6

    def name(self) -> Text:
        return "PlotCompareToCountry"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your average DNT is similar to South Korea and higher than Iran by 3 procent point.")
        plotting.create_international_timeline_plot("Dates", "DNT (Median)", plotting.df, folder.baseFolder,
                              ["France", "Lyon (your hospital)", "Slovakia", "South Africa"], "Country", False)

        return []

class PlotCompareToCountry_alt(Action): #6_alt

    def name(self) -> Text:
        return "PlotCompareToCountry_alt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your average DNT is similar to South Korea and higher than Iran by 3 procent point.")
        plotting.create_international_timeline_plot("Dates", "DNT (Median)", plotting.df, folder.baseFolder,
                              ["France", "Lyon (your hospital)", "Slovakia", "South Africa"], "Country", True)

        return []

class PlotPatientOfImpact_Timeline(Action): #9

    def name(self) -> Text:
        return "PlotPatientOfImpact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="The biggest reason I can see can be the increased amount of patients you have had recently.")


        return []

class PlotPatientOfImpact_barplot(Action): #11

    def name(self) -> Text:
        return "PlotPatientOfImpact_barplot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="The biggest reason I can see can be the increased amount of patients you have had recently.")
        plotting.dnt_barplot_bycountry("Hospital", "Patient Intake", plotting.df, folder.baseFolder)
        #MAKE A BARPLOT
        return []

class PlotCompareLocalHospitals(Action): #10

    def name(self) -> Text:
        return "PlotCompareLocalHospitals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        plotting.dnt_barplot_bycountry("Hospital", "DNT (Mean)", plotting.df, folder.baseFolder)
        dispatcher.utter_message(text="Your Mean DNT is 5 min higher than the average of local hospitals.")


        return []


class PlotTimelineOfPatientsIn(Action):#12

    def name(self) -> Text:
        return "PlotTimelineOfPatientsIn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is the timeline for Patients in care!")
        plotting.dnt_timeline(plotting, "Dates", "Patient Intake", plotting.df, folder.baseFolder, ["Lyon"], "Hospital")
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
                                       ["Lyon"], "Hospital")
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
                                       ["France", "Lyon (your hospital)"], "Country")
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
                                       ["France", "Lyon (your hospital)", "Slovakia", "South Africa"], "Country", False)
        #MAKE PLOT FOR THIS
        return []

class CompareInVsOutLocal(Action):#14

    def name(self) -> Text:
        return "CompareInVsOutLocal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is a comparison with local hospitals!")
        #plotting.linePlot("Dates", "DNT (Median)", "Country", "Hospital", plotting.df, folder.baseFolder)
        #MAKE PLOT FOR THIS
        return []

class CompareInVsOutInternational(Action):#15

    def name(self) -> Text:
        return "CompareInVsOutInternational"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is a comparison with International hospitals!")
        #plotting.linePlot("Dates", "DNT (Median)", "Country", "Hospital", plotting.df, folder.baseFolder)
        #MAKE PLOT FOR THIS

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
            int(DNT_Goal)
            # plotting.linePlot("Dates", "DNT (Median)", "Country", "Hospital", plotting.df, folder.baseFolder)
            # MAKE PLOT FOR THIS
            dispatcher.utter_message(text="Thanks for the discussion, looking forward to the next session!")
            return []



