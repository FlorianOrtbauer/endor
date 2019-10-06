from django.db import models
from django.utils.timezone import now
from django.apps import apps

class MissionManager(models.Manager):

    # CREATE TASK from mission
    def createTask(self):
        # get Task model (avoiding circular import via top lvl import)
        Task = apps.get_model(app_label='millenniumfalcon', model_name='Task')

        # can only create if mission status is IDLE
        # mission status is ACTIVE once a task is created
        if(self.status == 'i'):
            #create new task
            task = Task(mission_id=self.id, status='c', due_date=self.next_due)

            #change mission status to ACTIVE
            self.status = 'a'
            
            #persist changes
            self.save()
            task.save()
        return self


class TaskManager(models.Manager):

    # START task
    def start(self):
        # can only start task if in status CREATED or PLANNED
        if(self.status in ('c', 'p')):
            self.status = 's'
            self.actual_start = now()

            # persist changes
            self.save()
        return self
    
    # DEFER task
    def defer(self):
        # can only defer task if in status PLANNED or STARTED
        if(self.status in ('p', 's')):
            self.status = 'd'
            self.actual_start = now()
            
            #persist changes
            self.save()
        return self

    # FINISH task   
    def finish(self):

        # get Mission model (avoiding circular import via top lvl import)
        Mission = apps.get_model(app_label='millenniumfalcon', model_name='Mission')

        # can only finish task if in status STARTED
        if(self.status in ('s')):
            # set status to finished
            self.status = 'f'
    
            # get parent mission
            mission = Mission.objects.filter(id__exact=self.mission_id)
            # reset to IDLE
            mission.status = 'i'
            # update mission stats
            mission.last_execution = now()
            mission.last_duration = '10min'#TODO: create logic to extract duration out of Task actual start and DLM when finished.
            mission.next_due = now()#TODO: create logic to determine next due date based on mission interval and last execution.

            #persist changes
            self.save()
            mission.save()
        return self
