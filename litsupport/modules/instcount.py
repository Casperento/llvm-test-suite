"""Test module to collect code size metrics of the benchmark executable."""
import os


def _getInstCount(context):
    testname = context.test.getSourcePath()
    testdirname = os.path.dirname(testname)
    targetbasename = os.path.basename(os.path.splitext(testname)[0])
    filepath = os.path.join(testdirname, f'{targetbasename}.instcount')
    metrics = {'instcount': 0}
    if os.path.exists(filepath):
        with open(filepath, 'r') as fp:
            line = fp.readline().strip()
            if line == '':
                return metrics
            instcount = line.split(' instcount')
            metrics['instcount'] = int(instcount[0])
    return metrics


def mutatePlan(context, plan):
    plan.metric_collectors.append(_getInstCount)
