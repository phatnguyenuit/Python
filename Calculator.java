
/**
 * Calculator
 */
import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;
import javax.script.ScriptException;

public class Calculator {
    public static void main(String[] args) throws ScriptException {
        ScriptEngineManager mgr = new ScriptEngineManager();
        ScriptEngine engine = mgr.getEngineByName("JavaScript");
        String foo = "40+8/2+9*2/3-12";
        System.out.println(engine.eval(foo));
    }
}