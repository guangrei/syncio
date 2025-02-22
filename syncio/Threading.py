# -*-coding:utf8;-*-
from threading import Thread
from syncio.Task import NewTask, TaskOutput


def thread_gather(*args: NewTask) -> TaskOutput:
    ret = {}
    tasklist = []

    def runner(tasker: NewTask, task_id: int) -> None:
        task_id += 1
        result = tasker.func(*tasker.args, **tasker.kwargs)
        ret[f"task_{task_id}"] = result

    for k, f in enumerate(args):
        p = Thread(target=runner, kwargs={"tasker": f, "task_id": k})
        p.start()
        tasklist.append(p)
    for p in tasklist:
        p.join()

    return TaskOutput(ret)
