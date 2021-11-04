from game.action import Action

# TODO: Define the DrawActorsAction class here
class DrawActorsAction(Action):
    
    
    def __init__(self,output_service):
        self.output_service = output_service
    
    def execute(self,cast):
        robot = cast["robot"]
        marquee = cast["marquee"]
        artifacts = cast["artifact"]
        self.output_service.clear_screen()
        self.output_service.draw_actors(robot)
        self.output_service.draw_actors(artifacts)
        self.output_service.draw_actors(marquee)
        self.output_service.flush_buffer()
