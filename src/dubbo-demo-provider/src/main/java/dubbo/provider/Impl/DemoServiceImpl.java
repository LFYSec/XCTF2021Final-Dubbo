package dubbo.provider.Impl;

import dubbo.service.DemoService;
import org.apache.dubbo.config.annotation.Service;
import org.apache.dubbo.rpc.RpcContext;

@Service(version = "1.0.0")
public class  DemoServiceImpl implements DemoService {

    @Override
    public String sayHello(String name) {
        return "Hello " + name + ", response from provider: " + RpcContext.getContext().getLocalAddress();
    }

}
