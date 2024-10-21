"""Test module to collect code size metrics of the benchmark executable."""
import os


def sumInstCount(filepath, metrics):
    with open(filepath, 'r') as fp:
        for line in fp:
            line = line.strip()
            if line == '':
                continue
            instcount = line.split(' instcount')
            metrics['instcount'] = int(instcount[0])


def _getInstCount(context):
    metrics = {'instcount': 0}
    testname = context.test.getSourcePath()
    testdirname = os.path.dirname(testname)
    targetname = os.path.basename(os.path.splitext(testname)[0])
    if os.path.exists(testdirname):
        for ff in os.listdir(testdirname):
            if ff == f'{targetname}.instcount':
                filepath = os.path.join(testdirname, ff)
                sumInstCount(filepath, metrics)
    return metrics


def mutatePlan(context, plan):
    plan.metric_collectors.append(_getInstCount)
