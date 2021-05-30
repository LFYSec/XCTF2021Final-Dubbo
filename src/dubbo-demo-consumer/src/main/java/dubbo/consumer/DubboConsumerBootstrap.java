package dubbo.consumer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;

@SpringBootApplication(scanBasePackages = "dubbo.consumer")
public class DubboConsumerBootstrap {

    private final Logger logger = LoggerFactory.getLogger(getClass());

    public static void main(String[] args) {
        new SpringApplicationBuilder(DubboConsumerBootstrap.class)
                .run(args);
    }

}
