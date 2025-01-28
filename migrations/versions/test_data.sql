-- Добавление тестовых данных в таблицу users
INSERT INTO users (id, email, hashed_password) VALUES
(1, 'user1@example.com', 'hashed_password_1'),
(2, 'user2@example.com', 'hashed_password_2');

-- Добавление тестовых данных в таблицу hotels
INSERT INTO hotels (id, name, location, services, rooms_quantity, image_id) VALUES
(1, 'Hotel Sunshine', 'Miami', '{"wifi": true, "pool": true}', 10, 1),
(2, 'Mountain Retreat', 'Denver', '{"wifi": true, "spa": true}', 5, 2),
(3, 'City Center Inn', 'New York', '{"wifi": true, "gym": true}', 20, 3),
(4, 'Beachside Resort', 'Los Angeles', '{"wifi": true, "beach_access": true}', 15, 4),
(5, 'Forest Lodge', 'Seattle', '{"wifi": true, "hiking": true}', 8, 5),
(6, 'Urban Escape', 'Chicago', '{"wifi": true, "restaurant": true}', 12, 6);

-- Добавление тестовых данных в таблицу rooms
INSERT INTO rooms (id, hotel_id, name, description, price, services, quantity, image_id) VALUES
(1, 1, 'Deluxe Room', 'Просторный номер с видом на океан', 150.00, '{"air_conditioning": true, "tv": true}', 5, 1),
(2, 1, 'Standard Room', 'Уютный номер с базовыми удобствами', 100.00, '{"air_conditioning": true}', 5, 2),
(3, 1, 'Ocean View Suite', 'Сuite с видом на океан и балконом', 250.00, '{"air_conditioning": true, "tv": true, "mini_bar": true}', 3, 3),
(4, 2, 'Mountain View Room', 'Номер с видом на горы', 120.00, '{"tv": true}', 3, 4),
(5, 2, 'Spa Room', 'Номер с доступом к спа-процедурам', 200.00, '{"tv": true, "spa_access": true}', 2, 5),
(6, 3, 'City View Room', 'Номер с видом на городской пейзаж', 180.00, '{"tv": true, "mini_bar": true}', 10, 6),
(7, 4, 'Beachfront Room', 'Номер на пляже с прямым доступом к морю', 220.00, '{"tv": true, "beach_access": true}', 4, 7),
(8, 5, 'Forest Cabin', 'Кабинка в лесу с уютной атмосферой', 130.00, '{"fireplace": true}', 3, 8),
(9, 6, 'Urban Studio', 'Современная студия в центре города', 160.00, '{"kitchenette": true}', 5, 9),
(10, 6, 'Luxury Suite', 'Роскошный номер с отдельной спальней', 300.00, '{"air_conditioning": true, "tv": true, "mini_bar": true}', 2, 10);

-- Добавление тестовых данных в таблицу bookings
INSERT INTO bookings (id, room_id, user_id, date_from, date_to, price) VALUES
(1, 1, 1, '2023-09-01', '2023-09-05', 150.00),
(2, 5, 2, '2023-09-10', '2023-09-12', 130.00);
