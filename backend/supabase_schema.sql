create extension if not exists "uuid-ossp";

create table roles (
  id serial primary key,
  name text unique not null -- 'member', 'coach', 'admin'
);

create table users (
  id uuid primary key default uuid_generate_v4(),
  email text unique not null,
  password_hash text not null,
  full_name text,
  role_id integer references roles(id),
  created_at timestamptz default now()
);

create table memberships (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references users(id),
  status text check (status in ('active', 'inactive', 'expired')),
  start_date date,
  end_date date,
  created_at timestamptz default now()
);

create table exercise_routines (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references users(id),
  coach_id uuid references users(id),
  date date not null,
  routine jsonb,
  created_at timestamptz default now()
);

create table diet_plans (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references users(id),
  coach_id uuid references users(id),
  plan jsonb,
  created_at timestamptz default now()
);

create table meal_logs (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references users(id),
  date date not null,
  meal jsonb,
  macros jsonb,
  created_at timestamptz default now()
);

create index idx_users_role_id on users(role_id);
create index idx_exercise_user_id on exercise_routines(user_id);
create index idx_meal_logs_user_id on meal_logs(user_id);
