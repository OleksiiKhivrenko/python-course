--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: macbookpro
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    fullname character varying(30) DEFAULT 'Noname'::character varying NOT NULL,
    films text[]
);


ALTER TABLE public.actors OWNER TO macbookpro;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: macbookpro
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO macbookpro;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: macbookpro
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: directors; Type: TABLE; Schema: public; Owner: macbookpro
--

CREATE TABLE public.directors (
    id integer NOT NULL,
    fullname character varying(30) DEFAULT 'Noname'::character varying NOT NULL,
    films text[]
);


ALTER TABLE public.directors OWNER TO macbookpro;

--
-- Name: director_id_seq; Type: SEQUENCE; Schema: public; Owner: macbookpro
--

CREATE SEQUENCE public.director_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.director_id_seq OWNER TO macbookpro;

--
-- Name: director_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: macbookpro
--

ALTER SEQUENCE public.director_id_seq OWNED BY public.directors.id;


--
-- Name: films; Type: TABLE; Schema: public; Owner: macbookpro
--

CREATE TABLE public.films (
    id integer NOT NULL,
    name text DEFAULT 'Noname'::character varying NOT NULL,
    directors character varying(30)[],
    actors character varying(30)[]
);


ALTER TABLE public.films OWNER TO macbookpro;

--
-- Name: films_id_seq; Type: SEQUENCE; Schema: public; Owner: macbookpro
--

CREATE SEQUENCE public.films_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_id_seq OWNER TO macbookpro;

--
-- Name: films_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: macbookpro
--

ALTER SEQUENCE public.films_id_seq OWNED BY public.films.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: macbookpro
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: directors id; Type: DEFAULT; Schema: public; Owner: macbookpro
--

ALTER TABLE ONLY public.directors ALTER COLUMN id SET DEFAULT nextval('public.director_id_seq'::regclass);


--
-- Name: films id; Type: DEFAULT; Schema: public; Owner: macbookpro
--

ALTER TABLE ONLY public.films ALTER COLUMN id SET DEFAULT nextval('public.films_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: macbookpro
--

COPY public.actors (id, fullname, films) FROM stdin;
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: macbookpro
--

COPY public.directors (id, fullname, films) FROM stdin;
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: macbookpro
--

COPY public.films (id, name, directors, actors) FROM stdin;
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: macbookpro
--

SELECT pg_catalog.setval('public.actors_id_seq', 1, false);


--
-- Name: director_id_seq; Type: SEQUENCE SET; Schema: public; Owner: macbookpro
--

SELECT pg_catalog.setval('public.director_id_seq', 1, false);


--
-- Name: films_id_seq; Type: SEQUENCE SET; Schema: public; Owner: macbookpro
--

SELECT pg_catalog.setval('public.films_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

