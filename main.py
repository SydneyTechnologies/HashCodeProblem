class Contributor:
    def __init__(self, name, skills, skillNumber):
        # skills here will be a dictionary with the key as the skill name
        # and the value as the skill level
        self.name = name
        self.skills = skills
        self.skillNumber = skillNumber

    def __str__(self):
        return self.name


class Projects:
    def __init__(self, projectName, duration, bestBefore, rRoles):
        # note that the rRoles here is a list of required roles to complete this project
        self.projectName = projectName
        self.duration = duration
        self.bestBefore = bestBefore
        self.rRoles = rRoles
