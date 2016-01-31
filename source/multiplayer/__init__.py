import initialization
import scripts
import mission_templates
import presentations
import troops
import coop_mission_templates
import coop_presentations
import coop_scripts
import scenes

scripts = initialization.scripts + scripts.scripts + coop_scripts.coop_scripts
mission_templates = mission_templates.mission_templates + coop_mission_templates.coop_mission_templates
presentations = presentations.presentations + coop_presentations.coop_presentations
troops = troops.troops
scenes = scenes.scenes
