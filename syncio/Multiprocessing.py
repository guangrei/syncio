# -*-coding:utf8;-*-
from multiprocessing import Process, Manager
from syncio.Task import NewTask, TaskOutput, TaskReturnException


def gather(*args: NewTask) -> TaskOutput:
    manager = Manager()
    ret = manager.dict()
    tasklist = []

    def runner(tasker: NewTask, task_id: int) -> None:
        task_id += 1
        try:
            result = tasker.func(*tasker.args, **tasker.kwargs)
        except BaseException as e:
            result = TaskReturnException(e)
        ret[f"task_{task_id}"] = result

    for k, f in enumerate(args):
        p = Process(target=runner, kwargs={"tasker": f, "task_id": k})
        p.start()
        tasklist.append(p)
    for p in tasklist:
        p.join()

    return TaskOutput(dict(ret))
