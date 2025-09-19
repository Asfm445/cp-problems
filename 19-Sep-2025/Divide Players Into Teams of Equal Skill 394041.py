# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        a=0
        b=len(skill)-1
        sum=0
        min=skill[a]+skill[b]
        t=True
        while a<b:
            if skill[a]+skill[b]==min:
                sum+=skill[a]*skill[b]
                a+=1
                b-=1
            else:
                t=False
                break
        return sum if t else -1
        """
        :type skill: List[int]
        :rtype: int
        """
        