# -*-coding:utf8;-*-
from multiprocessing import Process, Manager
from syncio.Task import NewTask, TaskOutput


def gather(*args: NewTask) -> TaskOutput:
    manager = Manager()
    ret = manager.dict()
    tasklist = []

    def runner(tasker: NewTask, task_id: int) -> None:
        task_id += 1
        result = tasker.func(*tasker.args, **tasker.kwargs)
        ret[f"task_{task_id}"] = result

    for k, f in enumerate(args):
        p = Process(target=runner, kwargs={"tasker": f, "task_id": k})
        p.start()
        tasklist.append(p)
    for p in tasklist:
        p.join()

    return TaskOutput(dict(ret))
