# File used to control the runtime flow of the engine
# It allows variable framerate and controls which functions are called in the mainScript

class runtime:
    # === Create runtime and define the window using parameters provided ===
    def __init__(self, name: str, width: int, height: int, color = (0, 0, 0)) -> "runtime":
        import core as engine
        import pygame

        self.m_clock = pygame.time.Clock()
        self.m_window = engine.window(name, width, height, self.m_clock, color)
        
        
        self.m_timeElapsed = 0
        self.m_fixedTime = 1 / 60
        
        # Start the script      
        from .mainScript import start  
        start(self.m_window)
        
        
    # === Update control flow ===
    def update(self) -> None:
        from .mainScript import fixedUpdate, update
        while self.m_window.isRunning():
            self.m_clock.tick(self.m_window.getTargetFramerate())
            
            # Try to get the elapsed time
            try:
                self.m_timeElapsed += (1 / self.m_clock.get_fps())
            except:
                pass
            
            # If the frametime is over 16ms then run fixedUpdate
            while self.m_timeElapsed >= 0:
                deltaTime = self.m_timeElapsed / self.m_fixedTime
                fixedUpdate(self.m_window, deltaTime)

                self.m_timeElapsed -= self.m_fixedTime
            
            #Update the screen
            update(self.m_window)

    # === End program ===
    def end(self) -> None:
        #End the script
        from .mainScript import end
        end()

