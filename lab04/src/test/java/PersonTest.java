import org.junit.Test;

import static org.junit.Assert.*;
import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class PersonTest {

    @Test
    public void height(){
        Person person = mock(Person.class);
        given(person.height()).willReturn(176.9f);
        float height = person.height();
        assertEquals(176.9f, height, 2);
    }

    @Test
    public void age(){
        Person person = mock(Person.class);
        when(person.age()).thenReturn(17);
        int age = person.age();
        assertEquals(17, age);
    }

    @Test
    public void isAdult(){
        Person person = mock(Person.class);
        given(person.isAdult()).willReturn(false);
        boolean state = person.isAdult();
        assertFalse(state);
    }

}
