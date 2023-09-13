class Version:
    '''Represents the version of a release
    
    Attributes: major, minor, revision
    '''
    def __init__(self, major=-1, minor=-1, revision=-1):
        self.major = major
        self.minor = minor
        self.revision = revision
    
    def rep(self):
        return '{}.{}.{}'.format(self.major, self.minor, self.revision).replace('-1', '').rstrip('.')
    
    def __lt__(self, other):
        return (self.major, self.minor, self.revision) \
            < (other.major, other.minor, other.revision)

def solution(l):
    '''Given a list of strings, returns a sorted list of Version objects'''
    version_list = []
    for elt in l:
        # Store the integers in elt in a list,
        # and feed the list into a Version object
        integers = [int(c) for c in elt.split('.')]
        version_list.append(Version(*integers))
    
    lst = sorted(version_list) # or version_list.sort() maybe?

    return [version.rep() for version in lst]