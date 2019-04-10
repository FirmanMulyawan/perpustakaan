--
-- PostgreSQL database dump
--

-- Dumped from database version 10.7
-- Dumped by pg_dump version 10.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: buku; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.buku (
    id_buku integer NOT NULL,
    nobuku integer NOT NULL,
    judul_buku character varying(100) NOT NULL,
    tahun_terbit integer NOT NULL,
    pengarang character varying(100) NOT NULL
);


ALTER TABLE public.buku OWNER TO postgres;

--
-- Name: buku_id_buku_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.buku_id_buku_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.buku_id_buku_seq OWNER TO postgres;

--
-- Name: buku_id_buku_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.buku_id_buku_seq OWNED BY public.buku.id_buku;


--
-- Name: peminjam; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.peminjam (
    peminjam_id integer NOT NULL,
    nama_peminjam character varying(50) NOT NULL,
    tanggal_pinjam timestamp without time zone NOT NULL,
    tanggal_pengembalian timestamp without time zone NOT NULL,
    judul_buku character varying(100) NOT NULL,
    nobuku integer NOT NULL
);


ALTER TABLE public.peminjam OWNER TO postgres;

--
-- Name: peminjam_peminjam_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.peminjam_peminjam_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.peminjam_peminjam_id_seq OWNER TO postgres;

--
-- Name: peminjam_peminjam_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.peminjam_peminjam_id_seq OWNED BY public.peminjam.peminjam_id;


--
-- Name: buku id_buku; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.buku ALTER COLUMN id_buku SET DEFAULT nextval('public.buku_id_buku_seq'::regclass);


--
-- Name: peminjam peminjam_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.peminjam ALTER COLUMN peminjam_id SET DEFAULT nextval('public.peminjam_peminjam_id_seq'::regclass);


--
-- Data for Name: buku; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.buku (id_buku, nobuku, judul_buku, tahun_terbit, pengarang) FROM stdin;
1	1	one piece	2	odha
2	2	batman	2007	perdi
\.


--
-- Data for Name: peminjam; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.peminjam (peminjam_id, nama_peminjam, tanggal_pinjam, tanggal_pengembalian, judul_buku, nobuku) FROM stdin;
1	firmanmulyawan	2018-02-02 00:00:00	2018-02-03 00:00:00	one piece	1
\.


--
-- Name: buku_id_buku_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.buku_id_buku_seq', 2, true);


--
-- Name: peminjam_peminjam_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.peminjam_peminjam_id_seq', 1, true);


--
-- Name: buku buku_judul_buku_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.buku
    ADD CONSTRAINT buku_judul_buku_key UNIQUE (judul_buku);


--
-- Name: buku buku_nobuku_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.buku
    ADD CONSTRAINT buku_nobuku_key UNIQUE (nobuku);


--
-- Name: buku buku_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.buku
    ADD CONSTRAINT buku_pkey PRIMARY KEY (id_buku);


--
-- Name: peminjam peminjam_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.peminjam
    ADD CONSTRAINT peminjam_pkey PRIMARY KEY (peminjam_id);


--
-- Name: peminjam peminjam_judul_buku_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.peminjam
    ADD CONSTRAINT peminjam_judul_buku_fkey FOREIGN KEY (judul_buku) REFERENCES public.buku(judul_buku);


--
-- Name: peminjam peminjam_nobuku_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.peminjam
    ADD CONSTRAINT peminjam_nobuku_fkey FOREIGN KEY (nobuku) REFERENCES public.buku(nobuku);


--
-- PostgreSQL database dump complete
--

