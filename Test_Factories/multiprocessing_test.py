from multiprocessing import Process
import os

txt = "Toto"

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print(txt)
    print("------------------")

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    print("lancement du process :")
    p.start()
    print("exec")
    p.join()
