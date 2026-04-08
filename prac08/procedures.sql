- upsert
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook c WHERE c.name = p_name) THEN
        UPDATE phonebook 
        SET phone = p_phone 
        WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) 
        VALUES(p_name, p_phone);
    END IF;
END;
$$;

-- массовая вставка
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    names TEXT[],
    phones TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        
        IF phones[i] ~ '^[0-9]+$' THEN
            CALL upsert_contact(names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Invalid: % - %', names[i], phones[i];
        END IF;

    END LOOP;
END;
$$;

-- удаление

CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook c
    WHERE c.name = p_value OR c.phone = p_value;
END;
$$;