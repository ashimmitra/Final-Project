PGDMP     -                    y            our_project    13.2    13.2     ,           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            -           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            .           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            /           1262    32998    our_project    DATABASE     o   CREATE DATABASE our_project WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE our_project;
                postgres    false            ?            1259    33181    index_slider    TABLE     ?   CREATE TABLE public.index_slider (
    id integer NOT NULL,
    title character varying(150) NOT NULL,
    description text NOT NULL,
    image character varying(100) NOT NULL
);
     DROP TABLE public.index_slider;
       public         heap    postgres    false            ?            1259    33179    index_slider_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.index_slider_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.index_slider_id_seq;
       public          postgres    false    223            0           0    0    index_slider_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.index_slider_id_seq OWNED BY public.index_slider.id;
          public          postgres    false    222            ?           2604    33184    index_slider id    DEFAULT     r   ALTER TABLE ONLY public.index_slider ALTER COLUMN id SET DEFAULT nextval('public.index_slider_id_seq'::regclass);
 >   ALTER TABLE public.index_slider ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    223    223            )          0    33181    index_slider 
   TABLE DATA           E   COPY public.index_slider (id, title, description, image) FROM stdin;
    public          postgres    false    223          1           0    0    index_slider_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.index_slider_id_seq', 2, true);
          public          postgres    false    222            ?           2606    33189    index_slider index_slider_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.index_slider
    ADD CONSTRAINT index_slider_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.index_slider DROP CONSTRAINT index_slider_pkey;
       public            postgres    false    223            )   @  x?3?|?l??e?,[?`پ??<Xޮ?`?
?? ???@?:0k9P	???r?)?? թ?a??)@#?!2?,?ֹ?????͇X????F????+??!N??{y/?T ?4x1?S?Z??9@?*????(P?v?ۖ??X?b??p_??-j"?X??0F3gqNfJj?~nbEQjqJjZbiNI?oF???wU|hqp?y??^VA:?'.gw>X??58?,[<??0]
v<2?????????6?9 _???bij`fd???Lt???Su???RtS+s?u????|͊?=??C?? >????? Jj?     