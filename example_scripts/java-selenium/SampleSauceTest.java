import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.WebDriver.By;


import java.net.URL;

public class SampleSauceTest {

  public static final String USERNAME = "dragoon013";
  public static final String ACCESS_KEY = "b89b7205-3aca-4af2-a618-9bab4c7bdebd";
  public static final String URL = "http://" + USERNAME + ":" + ACCESS_KEY + "@ondemand.saucelabs.com:80/wd/hub";

  public static void main(String[] args) throws Exception {

    DesiredCapabilities caps = DesiredCapabilities.chrome();
    caps.setCapability("platform", "Windows XP");
    caps.setCapability("version", "43.0");

    WebDriver driver = new RemoteWebDriver(new URL(URL), caps);

    /**
     * Goes to Sauce Lab's guinea-pig page and prints title
     */

    driver.get("localhost:8082");

    driver.findElement(By.id("game_area"));
    //    driver.fireEvent("//input[@id='game_area']", "keydown");

    System.out.println("title of page is: " + driver.getTitle());

    driver.quit();
  }
}
