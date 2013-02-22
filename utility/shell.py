import cmd, os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 
import beanstalk

class BeanstalkShell(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(Beanstalk Shell) $ '


    def do_inspect(self, repository_name):
        repository_id = beanstalk.api.repository.get_id_by_name(repository_name)
        if (repository_id is None):
            print "Repository not found"
            return False

        commits = beanstalk.api.changeset.find_from_repo(repository_id, 1, 50)
        envs = beanstalk.api.environment.find(repository_id)

        for i in range(0, len(envs)):
            env = envs[i]['server_environment']
            print "====================================================================================="
            print str(env['id']) + "\t" + env['branch_name'] + "\t" + env['name'] + "\t" + env['current_version']
            print "====================================================================================="

            for i in range(0, len(commits)): 
                commit = commits[i]['revision_cache']
                if commit['hash_id'] == env['current_version']:
                    print "There are " + str(i) + " revisions behind"
                    break
                print str(i+1) + " - \t" + commit['author'][:6] + "\t\t" + commit['revision'] + "\t" + commit['time'][:19] + "\t" + commit['message']
            print "\n"

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def default(self, args):
        print "This command is not supported. Type in 'help' for more information"

if __name__ == '__main__':
    domain = os.environ.get('BEANSTALK_DOMAIN')
    username = os.environ.get('BEANSTALK_USERNAME')
    password = os.environ.get('BEANSTALK_PASSWORD')
    beanstalk.setup(domain, username, password)

    BeanstalkShell().cmdloop()
