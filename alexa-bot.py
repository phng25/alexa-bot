import boto3
import logging
import json
 
#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
#define the connection
ec2 = boto3.resource('ec2')
 
def lambda_handler(event, context):
 
   # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
   filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
 
    #filter the instances
    #ec2 = boto3.client('ec2', region_name=region)
   instances = ec2.instances.filter(Filters=filters)
 
    #locate all running instances
    count = 0
    for instance in instances: 
        count += 1


   RunningInstances = [instance.id for instance in instances]
 
    #print the instances for logging purposes
   print (RunningInstances) 
 
    #make sure there are actually instances to shut down.
   if len(RunningInstances) > 0:
        #perform the shutdown
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
        #print shuttingDown
        print (str(count) + " instances have been shut down")

   else:
    print ("No instances are running")