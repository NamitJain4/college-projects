----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 03.09.2024 14:31:23
-- Design Name: 
-- Module Name: timing_block_tb - Behavioral
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


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity timing_block_tb is
end timing_block_tb;

architecture tb of timing_block_tb is
    component Timing_block
    Port (
        clk_in : in STD_LOGIC; -- 100 MHz input clock
        mux_select : out STD_LOGIC_VECTOR (1 downto 0); -- Signal for the mux
        anodes : out STD_LOGIC_VECTOR (3 downto 0) -- Anodes signal for display
    );
    end component;
    
    signal clock : STD_LOGIC := '0';
    signal a, b, c, d, e, f : STD_LOGIC;
begin
    UUT : Timing_block port map(clk_in => clock, mux_select(0) => a, mux_select(1) => b, anodes(0) => c, anodes(1) => d, anodes(2) => e, anodes(3) => f);
    change_clk: process
        begin
            wait for 5 ns;
            clock <= not clock;
    end process;
end tb;
