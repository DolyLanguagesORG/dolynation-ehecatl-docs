@startuml ERD_DolyNation
hide circle
skinparam linetype ortho
skinparam shadowing false

entity "users" as user {
  * **id** : SERIAL
  --
  * email : VARCHAR(254) <<UNIQUE>>
  * password : VARCHAR(255) <<hash Argon2id>>
  * full_name : VARCHAR(255)
  * role : VARCHAR(20) [STUDENT, ADMIN]
  * current_streak : INTEGER
  * last_streak_date : DATE
  * created_at : TIMESTAMP
  * updated_at : TIMESTAMP
  * deleted_at : TIMESTAMP
}

entity "auth_access_tokens" as token {
  * **id** : SERIAL
  --
  * tokenable_id : INTEGER <<FK users.id>>
  * type : VARCHAR(255) [refresh]
  * name : VARCHAR(255)
  * hash : VARCHAR(255)
  * abilities : TEXT
  * created_at : TIMESTAMP
  * updated_at : TIMESTAMP
  * last_used_at : TIMESTAMP
  * expires_at : TIMESTAMP
  * deleted_at : TIMESTAMP
}

entity "categories" as cat {
  * **id** : SERIAL
  --
  * slug : VARCHAR(50) <<UNIQUE>>
  * name : VARCHAR(50)
  * description : TEXT
  * is_global : BOOLEAN
  * created_by_user_id : INTEGER <<FK users.id, nullable>>
  * created_at : TIMESTAMP
}

entity "user_preferences" as pref {
  * **user_id** : INTEGER <<PK, FK users.id>>
  --
  * target_language : VARCHAR(10) [en, fr, es, it]
  * default_difficulty : VARCHAR(20) [easy, medium, hard]
  * default_length : VARCHAR(20) [short, medium, long]
  * updated_at : TIMESTAMP
}

entity "user_selected_categories" as user_cat {
  * **user_id** : INTEGER <<PK, FK users.id>>
  * **category_id** : INTEGER <<PK, FK categories.id>>
}

entity "readings" as reading {
  * **id** : SERIAL
  --
  * user_id : INTEGER <<FK users.id>>
  * category : VARCHAR(50) <<deprecada>>
  * category_id : INTEGER <<FK categories.id>>
  * language : VARCHAR(10) [en, fr, es, it]
  * length_type : VARCHAR(20) [short, medium, long]
  * prompt_hash : VARCHAR(64)
  * title : VARCHAR(255)
  * description : TEXT
  * content : TEXT
  * difficulty : VARCHAR(20) [easy, medium, hard]
  * word_count : INTEGER
  * status : VARCHAR(20) [pending, completed]
  * score : INTEGER <<legacy>>
  * passed : BOOLEAN <<legacy>>
  * user_response : TEXT <<legacy>>
  * feedback : TEXT <<legacy>>
  * created_at : TIMESTAMP
  * updated_at : TIMESTAMP
  * deleted_at : TIMESTAMP
}

entity "evaluations" as eval {
  * **id** : SERIAL
  --
  * reading_id : INTEGER <<FK readings.id, UNIQUE>>
  * user_id : INTEGER <<FK users.id>>
  * user_summary : TEXT
  * score : INTEGER [0-100]
  * passed : BOOLEAN
  * feedback : TEXT
  * main_ideas_coverage : TEXT
  * created_at : TIMESTAMP
}

entity "vocabulary_logs" as vocab {
  * **id** : SERIAL
  --
  * user_id : INTEGER <<FK users.id>>
  * reading_id : INTEGER <<FK readings.id, nullable>>
  * selected_text : VARCHAR(255)
  * original_sentence : TEXT
  * definition : TEXT
  * contextual_example : TEXT
  * created_at : TIMESTAMP
}

entity "prompt_logs" as plog {
  * **id** : SERIAL
  --
  * level : VARCHAR(20)
  * event : VARCHAR(100)
  * message : TEXT
  * seed : VARCHAR(255)
  * user_id : INTEGER <<FK users.id, nullable>>
  * text_id : INTEGER <<FK readings.id, nullable>>
  * params : JSONB
  * system_prompt : TEXT
  * user_prompt : TEXT
  * error_message : TEXT
  * error_stack : TEXT
  * duration_ms : INTEGER
  * created_at : TIMESTAMP
}

' ==========================================
' RELACIONES
' ==========================================
user ||--o| pref : "1:1 prefiere"
user ||--o{ token : "1:N posee"
user ||--o{ user_cat : "1:N selecciona"
cat  ||--o{ user_cat : "1:N pertenece"
user ||--o{ reading : "1:N genera"
cat  ||--o{ reading : "1:N clasifica"
reading ||--o| eval : "1:1 evalúa"
user ||--o{ eval : "1:N realiza"
user ||--o{ vocab : "1:N consulta"
reading ||--o{ vocab : "1:N contiene"
user ||--o{ plog : "1:N audita"
reading ||--o{ plog : "1:N registra"

@enduml
