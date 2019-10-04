from django.core.management.base import BaseCommand, CommandError
from millenniumfalcon.models import Mission 


pending_missions = Mission.objects.all()



#class Command(BaseCommand):

    # ToDo: Create logic that checks all missions in idle based on their last execution and the desired interval (interval via cron job). 
    # --> keep in mind KPIs to be considered in future
    # create tasks in status CREATED and set mission status to ACTIVE
    # task status PLANNED, ACTIVE and FINISHED will be event based - same as status reset of Mission to IDLE
    # useful code snippets from django poll online tutorial below

    #IDEA:  system parameters to define threshold to create mission-tasks before reaching the due-date of the mission
    #       based on that parameter, parametrisation of the cron job.
    #help = 'Planning job creating tasks out of missions'
    #def add_arguments(self, parser):
        #parser.add_argument('poll_ids', nargs='+', type=int)
    
    #def handle(self, *args, **options):
        #for poll_id in options['poll_ids']:
        #    try:
        #        poll = Poll.objects.get(pk=poll_id)
        #    except Poll.DoesNotExist:
        #        raise CommandError('Poll "%s" does not exist' % poll_id)

        #    poll.opened = False
        #    poll.save()

        #    self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
