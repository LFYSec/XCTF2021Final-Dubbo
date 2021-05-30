package dubbo.consumer.controller;

import dubbo.service.DemoService;
import org.apache.dubbo.config.annotation.Reference;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class IndexController {

    @Reference(version = "1.0.0", timeout = 10000)
    private DemoService demoService;

    @GetMapping(value = "/")
    public String index(String name) {
        return demoService.sayHello(name);
    }
}
