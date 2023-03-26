import subprocess
import urllib.request


class PyGeoweaverWrapper:
    process: subprocess
    filename: str = 'geoweaver.jar'
    download_url: str = "https://github.com/ESIPFed/Geoweaver/releases/download/latest/geoweaver.jar"

    def start(self) -> None:
        urllib.request.urlretrieve(self.download_url, filename=self.filename)
        self.process = subprocess.Popen(f'java -jar {self.filename}'.split(),
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
        stdout, stderr = self.process.communicate()
        print(
            stdout,
            stderr
        )

    def stop(self) -> None:
        self.process.kill()

