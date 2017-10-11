import json
import json_loader

class BuildBuilder(object):

    def __init__(self):
        self.heroes_json = json_loader.get_json("butcher.json")

    def get_builds_for_hero(self, hero):
        final_build = ''
        builds = self.heroes_json[hero]["builds"].keys()
        talents = self.heroes_json[hero]["talents"]
        for build in builds:
            final_build += '{}\n\t'.format(build)
            choices = self.heroes_json[hero]["builds"][build]
            for i, choice in enumerate(choices):
                tier = i+1
                for talent in talents:
                    if(talent["tier"] == tier and talent["choice"] == choice):
                        final_build += '{}\n'.format(talent["name"])