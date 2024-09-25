----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 27.08.2024 15:31:57
-- Design Name: 
-- Module Name: digital_display_tb - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library ieee;
use ieee.std_logic_1164.all;


entity digital_display_tb is
end digital_display_tb;

architecture tb of digital_display_tb is

    component digital_display
    Port ( 
        p : in STD_LOGIC;
        q : in STD_LOGIC;
        r : in STD_LOGIC;
        s : in STD_LOGIC;
        A : out STD_LOGIC;
        B : out STD_LOGIC;
        C : out STD_LOGIC;
        D : out STD_LOGIC;
        E : out STD_LOGIC;
        F : out STD_LOGIC;
        G : out STD_LOGIC
    );
    end component;
    signal p, q, r, s : std_logic; -- inputs
    signal A, B, C, D, E, F, G : std_logic; -- outputs
begin

    UUT : digital_display port map (p => p, q => q, r => r, s => s, A => A, B => B, C => C, D => D, E => E, F => F, G => G);
    p <= '0', '1' after 160ns;
    q <= '0', '1' after 80ns, '0' after 160ns, '1' after 240ns;
    r <= '0', '1' after 40ns, '0' after 80ns, '1' after 120ns, '0' after 160ns, '1' after 200ns, '0' after 240ns, '1' after 280ns;
    s <= '0', '1' after 20ns, '0' after 40ns, '1' after 60ns, '0' after 80ns, '1' after 100ns, '0' after 120ns, '1' after 140ns, '0' after 160ns, '1' after 180ns, '0' after 200ns, '1' after 220ns, '0' after 240ns, '1' after 260ns, '0' after 280ns, '1' after 300ns;
    
end tb;
